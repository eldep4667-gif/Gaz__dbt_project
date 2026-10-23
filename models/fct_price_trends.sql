{{ config(materialized='view') }}

select
    PRICE_DATE,
    SERIES_DESCRIPTION,
    PRICE_VALUE,
    UNITS,
    PRICE_YEAR,
    PRICE_MONTH,
    PRICE_QUARTER
from {{ ref('fct_natural_gas_prices') }}
where PRICE_VALUE is not null