import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import snowflake.connector


plt.style.use('dark_background')
sns.set_palette("viridis")

def generate_natural_gas_report():
    print("1. Connecting to Snowflake and fetching transformed data...")
    
   
    conn = snowflake.connector.connect(
        user='DESOUKY',
        password='Mohamed012##Mohamed012##',
        account='PJOSIDX-CN55177',
        warehouse='FINANCE_WH',
        database='FINANCE_DB',
        schema='STAGING' 
    )
    
    query = "SELECT * FROM fct_natural_gas_prices"
    df = pd.read_sql(query, conn)
    conn.close()
    
   
    df['PRICE_DATE'] = pd.to_datetime(df['PRICE_DATE'])
    df = df.sort_values('PRICE_DATE')
    
    print("\n" + "="*40)
    print("2. EXECUTIVE SUMMARY & KEY STATISTICS")
    print("="*40)
    
    
    summary = df.groupby('SERIES_DESCRIPTION')['PRICE_VALUE'].agg(
        Count='count',
        Mean_Price='mean',
        Median_Price='median',
        Min_Price='min',
        Max_Price='max',
        Std_Dev='std'
    ).reset_index()
    
    print(summary.to_string(index=False))
    print("="*40)
    
    print("\n3. Generating Analytical Charts...")
    
    
    plt.figure(figsize=(14, 7))
    for series in df['SERIES_DESCRIPTION'].unique():
        subset = df[df['SERIES_DESCRIPTION'] == series]
        plt.plot(subset['PRICE_DATE'], subset['PRICE_VALUE'], label=series, alpha=0.8, linewidth=1.2)
        
    plt.title('Natural Gas Prices & Futures Historical Trend (1993 - 2026)', fontsize=14, color='cyan', pad=15)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Price ($/MMBTU)', fontsize=12)
    plt.legend(loc='upper left', fontsize=9)
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.tight_layout()
    
    chart_path_1 = 'natural_gas_trend_report.png'
    plt.savefig(chart_path_1, dpi=300)
    plt.close()
    print(f"-> Saved Time Series chart as '{chart_path_1}'")
    
   
    if 'PRICE_CHANGE_PCT' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(df['PRICE_CHANGE_PCT'].dropna(), bins=100, kde=True, color='magenta')
        plt.title('Daily Price Percentage Change Distribution (Volatility)', fontsize=14, color='orange', pad=15)
        plt.xlabel('Daily Percentage Change (%)', fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        plt.xlim(-20, 20) 
        plt.grid(True, linestyle='--', alpha=0.3)
        plt.tight_layout()
        
        chart_path_2 = 'natural_gas_volatility.png'
        plt.savefig(chart_path_2, dpi=300)
        plt.close()
        print(f"-> Saved Volatility chart as '{chart_path_2}'")

    print("\n4. Report generation completed successfully! 🚀")

if __name__ == "__main__":
    generate_natural_gas_report()