# Data Engineering ZoomCamp Course Project - Cohort 2023

## Preface
This repository contains the course project for the Data Engineering Zoomcamp organized by the by [DataTalks.Club](https://datatalks.club/) community.
The project covers main data engineering skills taught in the course: 
- Workflow Orchestration: Data Lake, Prefect tool, ETL with GCP & Prefect
- Data Warehouse: BigQuery
- Analytics engineering: dbt (data build tool), BigQuery and dbt
- Batch processing: Spark

## Architecture Diagram

![Arquitetura_v2](https://user-images.githubusercontent.com/69354054/226065772-56a0a07a-aa5d-47e5-a9e6-926913099c0d.png)

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

## How to reproduce this project?

#### Step 1: Clone this repo
Clone the repo into your local machine:  
```bash
git clone git@github.com:tmaferreira/DataEngineeringZoomCampProject.git
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

```bash
# Delete infra after your work, to avoid costs on any running services
terraform destroy
```

