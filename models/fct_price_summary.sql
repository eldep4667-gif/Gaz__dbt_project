{{ config(materialized='view') }}

select
    SERIES_DESCRIPTION,
    count(*) as TOTAL_RECORDS,
    round(avg(PRICE_VALUE), 4) as AVG_PRICE,
    min(PRICE_VALUE) as MIN_PRICE,
    max(PRICE_VALUE) as MAX_PRICE,
    stddev(PRICE_VALUE) as PRICE_STDDEV
from {{ ref('fct_natural_gas_prices') }}
group by SERIES_DESCRIPTION