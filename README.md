# 📊 Natural Gas ELT & Analytics Pipeline (1993 - 2026)

An end-to-end Data Engineering and Analytics project processing historical natural gas spot and futures prices (EIA data, over 37,000 records). This pipeline demonstrates modern cloud data warehousing, transformation best practices, and exploratory data analysis.

---

## 🏗️ Architecture & Tech Stack
* **Data Extraction:** Python (Web Scraping / API requests)
* **Cloud Data Warehouse:** Snowflake (`FINANCE_DB` with RAW, STAGING, and ANALYTICS schemas)
* **Data Transformation:** dbt (Data Build Tool) for cleaning, standardizing, and calculating daily changes & volatility.
* **Data Analysis & Visualization:** Python (Pandas, NumPy, Matplotlib, Seaborn) inside Jupyter Notebooks.

---

## ⚙️ Pipeline Steps
1. **Ingestion:** Raw data fetched and loaded directly into Snowflake `RAW.NATURAL_GAS_PRICES_RAW`.
2. **Transformation (dbt):** 
   - Cleaned string fields and cast data types.
   - Built modular staging and fact models (`fct_natural_gas_prices`).
   - Calculated daily price differences and percentage changes using window functions (`LAG`).
3. **Analytics & Reporting:** Generated statistical summaries and high-resolution visualizations (Time Series Trends, Volatility Distributions, and Correlation Matrices).

---

## 📈 Visual Reports & Insights

### 1. Historical Price Trends (1993 - 2026)
![Natural Gas Trend](natural_gas_trend_report.png)

### 2. Price Volatility Distribution
![Volatility](natural_gas_volatility.png)

---
🚀 **Author:** Mohamed Desouky