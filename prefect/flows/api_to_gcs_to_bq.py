import os
import pandas as pd
import numpy as np
import time

from pathlib import Path
from prefect import flow, task
from prefect.tasks import task_input_hash
from datetime import timedelta, datetime
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp import GcpCredentials

@task(log_prints=True, tags=["extract"], cache_key_fn=task_input_hash, cache_expiration=timedelta(days=1))
def extract_data() -> pd.DataFrame:
    """Download US Accidentes data from Kaggle API into Pandas Dataframe"""
    
    download_dataset = os.system("mkdir dataset;cd dataset;kaggle datasets download -d 'sobhanmoosavi/us-accidents'")
    
    df = pd.read_csv('dataset/us-accidents.zip', compression='zip')

    columns_list = ['ID', 'Severity', 'Start_Time', 'End_Time', 'Description', 'Street', 'City', 'State', 'Country', 'Weather_Condition', 'Sunrise_Sunset']
    df_us_accidents = df.loc[:, df.columns.isin(columns_list)]

    return df_us_accidents

@task(log_prints=True)
def transform_data(df_us_accidents: pd.DataFrame) -> pd.DataFrame:
    """Fill missing values and fix dtypes"""
    
    print(f"Pre: Missing values: {df_us_accidents.isna().sum().sum()}")

    # Fill missing values with value "Unknown"
    columns_with_missing_values = ['Street', 'City', 'Weather_Condition', 'Sunrise_Sunset']
    df_us_accidents[columns_with_missing_values] = df_us_accidents[columns_with_missing_values].fillna('Unknown')
    df_us_accidents[columns_with_missing_values] = df_us_accidents[columns_with_missing_values].replace(np.nan, 'Unknown')

    print(f"Post: Missing values: {df_us_accidents.isna().sum().sum()}")

    # Convert some columns to string type
    df_us_accidents.ID = df_us_accidents.ID.astype('str')
    df_us_accidents.Description = df_us_accidents.Description.astype('str')
    df_us_accidents.Street = df_us_accidents.Street.astype('str')
    df_us_accidents.City = df_us_accidents.City.astype('str')
    df_us_accidents.State = df_us_accidents.State.astype('str')
    df_us_accidents.Country = df_us_accidents.Country.astype('str')
    df_us_accidents.Weather_Condition = df_us_accidents.Weather_Condition.astype('str')
    df_us_accidents.Sunrise_Sunset = df_us_accidents.Sunrise_Sunset.astype('str')

    # Convert some columns to date and time format
    df_us_accidents['Start_Date'] = pd.to_datetime(df_us_accidents['Start_Time']).dt.strftime('%Y-%m-%d')
    df_us_accidents['Start_Hour'] = pd.to_datetime(df_us_accidents['Start_Time']).dt.strftime('%H:%M:%S')

    df_us_accidents['End_Date'] = pd.to_datetime(df_us_accidents['End_Time']).dt.strftime('%Y-%m-%d')
    df_us_accidents['End_Hour'] = pd.to_datetime(df_us_accidents['End_Time']).dt.strftime('%H:%M:%S')

    df_us_accidents.drop(['Start_Time', 'End_Time'], axis="columns", inplace=True)
    
    return df_us_accidents

@task(log_prints=True)
def write_local(df_transformed: pd.DataFrame) -> Path:
    """Write dataframe locally as parquet file"""

    parquet_path = Path(f"dataset/us-accidents.parquet")
    df_transformed.to_parquet(parquet_path, compression="gzip")
    
    return parquet_path

@task(log_prints=True)
def write_gcs(parquet_path: Path) -> None:
    """Upload local parquet file into GCS Bucket"""
    gcp_cloud_storage_bucket_block = GcsBucket.load("gcs-connector-zoomcamp-finalproject")
    gcp_cloud_storage_bucket_block.upload_from_path(from_path=parquet_path, to_path=parquet_path)

    return

@task(log_prints=True)
def extract_from_gcs(parquet_path: Path) -> Path:
    """Download data from GCS"""
    gcp_cloud_storage_bucket_block = GcsBucket.load("gcs-connector-zoomcamp-finalproject")
    gcp_cloud_storage_bucket_block.get_directory(from_path=parquet_path, local_path=f"dataset/")
    
    return Path(f"{parquet_path}")

@task(log_prints=True)
def write_bq(path: Path) -> None:
    """Read parquet file and write dataframe to BigQuery"""
    df_final = pd.read_parquet(path)

    gcp_credentials_block = GcpCredentials.load("gcs-credentials-zoomcap-finalproject")

    df_final.to_gbq(
        destination_table="us_traffic_accidents_data.us_traffic_accidents",
        project_id="dezoomcamp-finalproject",
        credentials=gcp_credentials_block.get_credentials_from_service_account(),
        chunksize=500_000,
        if_exists="replace",
    )

    return

@flow(name="Ingest Data")
def main_flow(table_name: str = "us_accidents") -> None:
    """Main ETL flow to ingest data"""
    
    raw_data = extract_data()
    df_transformed = transform_data(raw_data)
    parquet_path = write_local(df_transformed)

    write_gcs(parquet_path)
    path = extract_from_gcs(parquet_path)
    write_bq(path)

if __name__ == "__main__":
    main_flow()
