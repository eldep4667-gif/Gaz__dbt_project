{{ config(materialized='view') }}

select
    PRICE_YEAR,
    SERIES_DESCRIPTION,
    round(avg(PRICE_VALUE), 4) as YEARLY_AVG_PRICE,
    max(PRICE_VALUE) as YEARLY_MAX_PRICE,
    min(PRICE_VALUE) as YEARLY_MIN_PRICE
from {{ ref('fct_natural_gas_prices') }}
group by PRICE_YEAR, SERIES_DESCRIPTION