{{ config(
        materialized = "view",  
        partition_by = {
            "field": "start_datetime",
            "data_type": "timestamp",
            "granularity": "year"
        },
        cluster_by = "country"
    ) 
}}

select
    -- identifiers
    {{ dbt_utils.surrogate_key(["ID"]) }} as accident_id,
    cast(severity as integer) as severity_id,

    -- timestamps
    cast(start_time as timestamp) as start_datetime,
    cast(end_time as timestamp) as end_datetime,

    -- accident info
    cast(description as string) as description,
    cast(street as string) as street,
    cast(city as string) as city,
    cast(state as string) as state,
    cast(country as string) as country,
    cast(weather_condition as string) as weather_condition,
    cast(sunrise_sunset as string) as sunrise_sunset

from {{ source("staging", "us_traffic_accidents") }}
