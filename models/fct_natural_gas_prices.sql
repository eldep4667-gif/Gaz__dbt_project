{{ config(materialized='view') }}

with source_data as (
    select * from {{ ref('stg_clean') }}
)

select
    PERIOD as PRICE_DATE,
    SERIES_DESCRIPTION,
    VALUE as PRICE_VALUE,
    UNITS,
    extract(year from PERIOD) as PRICE_YEAR,
    extract(month from PERIOD) as PRICE_MONTH,
    extract(quarter from PERIOD) as PRICE_QUARTER,
    lag(VALUE, 1) over (partition by SERIES_DESCRIPTION order by PERIOD) as PREV_DAY_PRICE,
    VALUE - PREV_DAY_PRICE as PRICE_CHANGE,
    round((PRICE_CHANGE / nullif(PREV_DAY_PRICE, 0)) * 100, 4) as PRICE_CHANGE_PCT
from source_data