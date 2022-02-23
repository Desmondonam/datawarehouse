# datawarehouse

## Building data warehouse techstack

Consisting of A “data warehouse” (mysql, sqlite) An orchestration service (Airflow) An ELT tool (dbt) A reporting environment (redash) Set it up locally using fully dockerized

Create a DAG in Airflow that uses the bash/python operator to load the data files into your database. Think about a useful separation of Prod, Dev and Staging Connect dbt with your DWH and write transformations codes for the data you can execute via the Bash or Python operator in Airflow. Write proper documentation for your data models and access the dbt docs UI for presentation. Check additional modules of dbt that can support you with data quality monitoring (e.g. great_expectations, dbt_expectations or re-data). Connect the reporting environment and create a dashboard out of this data Write a short article about your approach and what were the most important decisions along the way.


## Airflow turorial Master

This is an example of how airflow works. In this we have created the first DAGS and we have used GCP to show how 
the airflow works