{{ config(
        materialized = "table",  
        partition_by = {
            "field": "start_date",
            "data_type": "date",
            "granularity": "year"
        },
        cluster_by = "country"
    ) 
}}

select
    -- identifiers
    {{ dbt_utils.surrogate_key(["ID"]) }} as accident_id,
    cast(severity as integer) as severity_id,

     -- date and times
    cast(Start_Date as date) as start_date,
    cast(End_Date as date) as end_date,

    cast(Start_Hour as time) as start_time,
    cast(End_Hour as time) as end_time,

    -- accident info
    cast(description as string) as description,
    cast(street as string) as street,
    cast(city as string) as city,
    cast(state as string) as state,
    cast(country as string) as country,
    cast(weather_condition as string) as weather_condition,
    cast(sunrise_sunset as string) as sunrise_sunset

from {{ source("staging", "us_traffic_accidents") }}
