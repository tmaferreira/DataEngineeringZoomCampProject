# Data Engineering ZoomCamp Course Project - US Accidents

<p align="center">
  <img width="80%" src="https://static.vecteezy.com/system/resources/previews/002/395/151/original/modern-city-with-road-traffic-vector.jpg"/>
</p>

## Preface
This repository contains the course project for the Data Engineering Zoomcamp (Cohort 2023) organized by the by [DataTalks.Club](https://datatalks.club/) community.
The project covers main data engineering skills taught in the course: 
- Workflow Orchestration: Data Lake, Prefect tool, ETL with GCP & Prefect
- Data Warehouse: BigQuery
- Analytics engineering: dbt (data build tool), BigQuery and dbt
- Batch processing: Spark

## US Accidents Project

### Dataset
US car crash dataset (covers 49 states).
Crash data is collected from February 2016 to December 2021 using various APIs that provide streaming traffic incident (or event) data. These APIs transmit traffic data captured by a variety of entities, such as US and state departments of transportation, law enforcement agencies, traffic cameras, and traffic sensors on road networks. There are currently around 2.8 million crash records in this dataset.

The dataset has 47 columns, but for the present project I decided to select only the relevant columns for my analysis. The following columns will be used:

<div align="center">
  
| #  | Attribute             |                     Description                                      |
|:--:|:---------------------:|----------------------------------------------------------------------|
|  1 | **ID**                | This is a unique identifier of the accident record.                  |
|  2 | **Severity**          | Shows the severity of the accident, a number between 1 and 4. <br> 1 indicates the least impact on traffic (i.e., short delay as a result of the accident) and 4 indicates a significant impact on traffic (i.e., long delay).         |
|  3 | **Start_Time**        | Shows the start time of the accident in local time zone.             |
|  4 | **End_Time**          | Shows the end time of the accident in local time zone. <br> End time here refers to when the impact of accident on traffic flow was dismissed.                                                                                          |
|  5 | **Description**       | Shows the natural language description of the accident.	            |
|  6 | **Street**            | Shows the street name in address field.	                            |
|  7 | **City**              | Shows the city in address field.	                                    |
|  8 | **State**             | Shows the state in address field.	                                  |
|  9 | **Country**           | Shows the country in address field.                                  |
| 10 | **Weather_Condition** | Shows the weather condition (rain, snow, thunderstorm, fog, etc.)	  |
| 11 | **Sunrise_Sunset**    | Shows the period of day (i.e. day or night) based on sunrise/sunset.	|
  
</div>

More information about this dataset: [Author blog](https://smoosavi.org/datasets/us_accidents) and [Kaggle](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents)

#### Dataset Acknowledgments
- Moosavi, Sobhan, Mohammad Hossein Samavatian, Srinivasan Parthasarathy, and Rajiv Ramnath. “A Countrywide Traffic Accident Dataset.”, 2019.
- Moosavi, Sobhan, Mohammad Hossein Samavatian, Srinivasan Parthasarathy, Radu Teodorescu, and Rajiv Ramnath. "Accident Risk Prediction based on Heterogeneous Sparse Data: New Dataset and Insights." In proceedings of the 27th ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems, ACM, 2019.

### Architecture Diagram

<p align="center">
  <img width="60%" src="https://user-images.githubusercontent.com/69354054/226065772-56a0a07a-aa5d-47e5-a9e6-926913099c0d.png"/>
</p>

### Technologies Used
- **Google Cloud Platform (GCP)**:
  - **Google Cloud Storage (GCS)**: Data Lake
  - **BigQuery**: Data Warehouse
- **Terraform**: Infrastructure as code (IaC)
- **dbt**: Data Transformation
- **Pandas**: Data Analysis & Exploration
- **Prefect**: Workflow Orchestration
- **Looker Studio**: Visualize Data

### DW Table Structure
<div align="center">
  
| #  | Attribute             |                     Description                                      |
|:--:|:---------------------:|----------------------------------------------------------------------|
|  1 | **accident_id**       | This is a unique identifier of the accident record.                  |
|  2 | **severity_id**       | Shows the severity of the accident, a number between 1 and 4. <br> 1 indicates the least impact on traffic (i.e., short delay as a result of the accident) and 4 indicates a significant impact on traffic (i.e., long delay).         |
|  3 | **start_date**        | Shows start date of the accident was started.                        |
|  4 | **end_date**          | Shows the end date of the accident was ended.                        |
|  5 | **start_time**        | Shows the start time of the accident in local time zone.             |
|  6 | **end_time**          | Shows the end time of the accident in local time zone. <br> End time here refers to when the impact of accident on traffic flow was dismissed.                                                                                          |
|  7 | **description**       | Shows the natural language description of the accident.	            |
|  8 | **street**            | Shows the street name in address field.	                            |
|  9 | **city**              | Shows the city in address field.	                                    |
| 10 | **state**             | Shows the state in address field.	                                  |
| 11 | **country**           | Shows the country in address field.                                  |
| 12 | **weather_condition** | Shows the weather condition (rain, snow, thunderstorm, fog, etc.)	  |
| 13 | **sunrise_sunset**    | Shows the period of day (i.e. day or night) based on sunrise/sunset.	|
</div>

![image](https://user-images.githubusercontent.com/69354054/231012310-0f2b2540-e59d-4910-97b5-5c62c8803637.png)

**Partitioning and Clustering:**
![image](https://user-images.githubusercontent.com/69354054/231012117-8d3dc96a-9e35-4443-84a6-e05cd30cbf29.png)

- Partition by column **start_date**, more specifically by **year** to obtain annual granularity
- Clustering by column **country** to group data that have the same country value

Benefits of combining clustered and partitioned tables: [Combining clustered and partitioned tables](https://cloud.google.com/bigquery/docs/clustered-tables#combining_clustered_and_partitioned_tables)

### Data visualization: Dashboards

#### Main Questions
1. Which State/City/Street in US has reported most number of Accident Cases between 2016 and 2021?
2. How are the weather conditions in most of the accident cases in US?
3. Did most accidents occur at night or during the day?

#### US Crash Accidents by State, City and Street - Dashboard

![image](https://user-images.githubusercontent.com/69354054/232915603-cbebe236-c9a8-4057-a980-fa5cb853fff5.png)

#### US Crash Accidents by Severity, Weather Conditions, Day/Night and Date (Year and Month)

![image](https://user-images.githubusercontent.com/69354054/232915741-2d1ca625-b6bd-4893-bf4f-731b796cc518.png)

**More detailed analysis of the results obtained: [Data Analysis](https://github.com/tmaferreira/DataEngineeringZoomCampProject/blob/main/DataAnalysis/Dashboards.md)**

## How to reproduce this project?

#### Step 1: Clone this repo and install necessary requirements
1. Clone the repo into your local machine:  
```bash
git clone git@github.com:tmaferreira/DataEngineeringZoomCampProject.git
```
2. Install all required dependencies into your environment
```bash
pip3 install -r requirements.txt
```

#### Step 2: Setup of GCP
1. Create a [Google Cloud Platform (GCP)](https://cloud.google.com/) free account with your Google e-mail
2. Create a new GCP project with the name **dezoomcamp-finalproject** (Note: Save the assigned Project ID. Projects have a unique ID and for that reason another ID will be assigned)
3. Create a Service Account:
    - Go to **IAM & Admin > Service accounts > Create service account**
    - Provide a service account name and grant the roles: **Viewer** + **BigQuery Admin** + **Storage Admin** + **Storage Object Admin**
    - Download the Service Account json file
    - Download [SDK](https://cloud.google.com/sdk/docs/install-sdk) for local setup
    - Set environment variable to point to your downloaded GCP keys:
    ```bash
    export GOOGLE_APPLICATION_CREDENTIALS="<path/to/your/service-account-authkeys>.json"
    ```
    ```bash
    # Refresh token/session, and verify authentication
    gcloud auth application-default login
    ```
    
4. Enable the following APIs:
    - [Identity and Access Management (IAM) API](https://console.cloud.google.com/apis/library/iam.googleapis.com)
    - [IAM Service Account Credentials API](https://console.cloud.google.com/apis/library/iamcredentials.googleapis.com)


#### Step 3: Creation of a GCP Infrastructure
1. Install [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)
2. Copy files (**main.tf** and **variables.tf**) for the infrastructure creation (Use files created in Zoomcamp course: [Terraform files](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/week_1_basics_n_setup/1_terraform_gcp/terraform))
3. In the file variables.tf change variable **BQ_DATASET** to: **us_traffic_accidents_data**
4. Execute the following commands to plan the creation of the GCP infrastructure:
```bash
# Initialize state file (.tfstate)
terraform init

# Check changes to new infra plan
# -var="project=<your-gcp-project-id>"

terraform plan -var="project=dezoomcamp-finalproject"
```

```bash
# Create new infra
# -var="project=<your-gcp-project-id>"

terraform apply -var="project=dezoomcamp-finalproject"
```

It is possible to see in the GCP console that the Infrastructure was correctly created.

#### Step 4: Setup of Kaggle API
1. Create a [Kaggle](https://www.kaggle.com/) free account
2. Create an API token:
    - Click on your avatar
    - Go to Account menu
    - Click on the option "Create New API Token"
    - Download the json file for local setup

3. In your local setup, copy the file into the path: 
```bash
~/.kaggle/
```
4. For your security, ensure that other users of your computer do not have read access to your credentials:
```bash
chmod 600 ~/.kaggle/kaggle.json
```

To see all available API options and commands:
```bash
 kaggle --help
 ```

#### Step 5: Setup orchestration using Prefect
1. Setup the prefect server so that you can access the UI. Run the following command in a CL terminal:
```bash
 prefect orion start
 ```
2. Access the UI in your browser: **http://127.0.0.1:4200/**
3. For the connection with GCP Buckets it is necessary to create a block:
  - In the side menu click on the option **Blocks**
  - Click on the '+' button and select the **GCS Bucket** option
  - Fill in the required fields:
    <img width="925" alt="image" src="https://user-images.githubusercontent.com/69354054/229305723-a3ef5438-33d6-4111-94e2-d5aa9165fd14.png">

  - In the **Gcp Credentials** field click on the **Add** button
  - Fill in the **Block Name** field:
    <img width="925" alt="image" src="https://user-images.githubusercontent.com/69354054/229306009-5e698082-e3cf-4e53-be74-d26e89e26f8f.png">
  
  - Using the service account json file that was downloaded in step 2, copy its content and paste it in the **Service Account Info** field
  - Click on the **Create** button and you will be redirected to the previous GCS Bucket block creation page:
  - In the **Gcp Credentials** field select the Gcp credential created previously:
    <img width="925" alt="image" src="https://user-images.githubusercontent.com/69354054/229306194-2c3b0517-4ec9-4293-bffc-31a153741f29.png">
  
  - Click on the **Create** button to create the block
  
4. To execute the flow, run the following commands in a different CL terminal than step 1:
```bash
python prefect/flows/api_to_gcs_to_bq.py
 ```
 
#### Step 6: Running the dbt flow
1. Create a [dbt cloud](https://www.getdbt.com/product/what-is-dbt/) free account
2. Clone this repo
3. In the command line of dbt running the following command:
```bash
dbt run
```

**dbt lineage generated:**

<p align="center">
  <img width="70%" src="https://user-images.githubusercontent.com/69354054/231011761-b58f7bf3-9789-4d85-9c4a-1716829d963c.png"/>
</p>

### Validation of created tables

#### Production Table

**Check Data in BigQuery**:
- The data will be available at **dezoomcamp-finalproject.dbt_us_traffic_accidents**
- The production version will be available at **dezoomcamp-finalproject.production.dim_us_traffic_accidents** (dimension table) and **dezoomcamp-finalproject.production.stg_us_traffic_accidents** (staging table)

<p align="center">
  <img width="30%" src="https://user-images.githubusercontent.com/69354054/231011864-133e391e-ea48-465d-8f31-812aa28ca18f.png"/>
</p>

### Improvements
- Add unit tests
- Add CI/CD pipeline
