{{ config(materialized='view') }}

select
    PRICE_DATE,
    SERIES_DESCRIPTION,
    PRICE_VALUE,
    PREV_DAY_PRICE,
    PRICE_CHANGE,
    PRICE_CHANGE_PCT
from {{ ref('fct_natural_gas_prices') }}
where PRICE_CHANGE_PCT is not null