# Data Engineering ZoomCamp Course Project - Cohort 2023

## Preface
This repository contains the course project for the Data Engineering Zoomcamp organized by the by [DataTalks.Club](https://datatalks.club/) community.
The project covers main data engineering skills taught in the course: 
- Workflow Orchestration: Data Lake, Prefect tool, ETL with GCP & Prefect
- Data Warehouse: BigQuery
- Analytics engineering: dbt (data build tool), BigQuery and dbt
- Batch processing: Spark

## Architecture Diagram

![Arquitetura_v1](https://user-images.githubusercontent.com/69354054/224508395-02dfd148-126a-4e91-96ee-b6b58df1502f.png)

## Technologies
- **Google Cloud Platform (GCP)**:
  - **Google Cloud Storage (GCS)**: Data Lake
  - **BigQuery**: Data Warehouse
- **dbt**: Data Transformation
- **Spark**: Distributed Processing
- **SQL**: Data Analysis & Exploration
- **Prefect**: Workflow Orchestration
- **Looker Studio**: Visualize Data

## Dataset
US car crash dataset (covers 49 states).
Crash data is collected from February 2016 to December 2021 using various APIs that provide streaming traffic incident (or event) data. These APIs transmit traffic data captured by a variety of entities, such as US and state departments of transportation, law enforcement agencies, traffic cameras, and traffic sensors on road networks. There are currently around 2.8 million crash records in this dataset.

More information about this dataset: [Author blog](https://smoosavi.org/datasets/us_accidents) and [Kaggle](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents)

#### Dataset Acknowledgments
- Moosavi, Sobhan, Mohammad Hossein Samavatian, Srinivasan Parthasarathy, and Rajiv Ramnath. “A Countrywide Traffic Accident Dataset.”, 2019.
- Moosavi, Sobhan, Mohammad Hossein Samavatian, Srinivasan Parthasarathy, Radu Teodorescu, and Rajiv Ramnath. "Accident Risk Prediction based on Heterogeneous Sparse Data: New Dataset and Insights." In proceedings of the 27th ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems, ACM, 2019.


