"""
Sales Data Analysis Script
This script performs data analysis and visualization on a sample sales dataset.
"""

# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

def create_sample_data():
    """Create a sample sales dataset"""
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Create sample sales data
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    n_records = len(dates)
    
    # Generate sample data
    data = {
        'Date': dates,
        'Product': np.random.choice(['Electronics', 'Clothing', 'Books', 'Food'], n_records),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], n_records),
        'Sales': np.random.normal(1000, 200, n_records),
        'Units': np.random.randint(10, 100, n_records)
    }
    
    # Create DataFrame and add some missing values for demonstration
    df = pd.DataFrame(data)
    mask = np.random.random(n_records) < 0.05
    df.loc[mask, 'Sales'] = np.nan
    
    return df

def explore_and_clean_data(df):
    """Explore and clean the dataset"""
    print("=== Data Exploration and Cleaning ===\n")
    
    print("Dataset Info:")
    print(df.info())
    
    print("\nMissing values in each column:")
    print(df.isnull().sum())
    
    # Clean the dataset by filling missing values with median
    df['Sales'] = df['Sales'].fillna(df['Sales'].median())
    
    print("\nVerifying no missing values remain:")
    print(df.isnull().sum())
    
    return df

def perform_basic_analysis(df):
    """Perform basic statistical analysis"""
    print("\n=== Basic Statistical Analysis ===\n")
    
    print("Basic statistics for numerical columns:")
    print(df.describe())
    
    # Group by Product and calculate mean sales
    print("\nAverage sales by product category:")
    product_sales = df.groupby('Product')['Sales'].agg(['mean', 'count', 'std']).round(2)
    print(product_sales)
    
    # Group by Region and calculate mean sales
    print("\nAverage sales by region:")
    region_sales = df.groupby('Region')['Sales'].agg(['mean', 'count', 'std']).round(2)
    print(region_sales)
    
    # Monthly sales analysis
    df['Month'] = df['Date'].dt.strftime('%Y-%m')
    monthly_sales = df.groupby('Month')['Sales'].sum().round(2)
    print("\nMonthly sales totals:")
    print(monthly_sales)
    
    return product_sales, region_sales, monthly_sales

def create_visualizations(df, product_sales, monthly_sales):
    """Create various visualizations"""
    print("\n=== Creating Visualizations ===\n")
    
    # Set the style for all plots
    plt.style.use('seaborn')
    sns.set_palette('husl')
    
    # Create a figure with subplots
    fig = plt.figure(figsize=(20, 15))
    
    # 1. Line chart: Monthly sales trend
    plt.subplot(2, 2, 1)
    monthly_sales.plot(kind='line', marker='o')
    plt.title('Monthly Sales Trend')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    
    # 2. Bar chart: Average sales by product category
    plt.subplot(2, 2, 2)
    product_sales['mean'].plot(kind='bar')
    plt.title('Average Sales by Product Category')
    plt.xlabel('Product Category')
    plt.ylabel('Average Sales')
    plt.xticks(rotation=45)
    
    # 3. Histogram: Distribution of daily sales
    plt.subplot(2, 2, 3)
    sns.histplot(data=df, x='Sales', bins=30)
    plt.title('Distribution of Daily Sales')
    plt.xlabel('Sales Amount')
    plt.ylabel('Frequency')
    
    # 4. Box plot: Sales distribution by region
    plt.subplot(2, 2, 4)
    sns.boxplot(data=df, x='Region', y='Sales')
    plt.title('Sales Distribution by Region')
    plt.xlabel('Region')
    plt.ylabel('Sales')
    
    # Adjust layout and display
    plt.tight_layout()
    plt.show()

def print_key_findings(df, product_sales, region_sales, monthly_sales):
    """Print key findings from the analysis"""
    print("\n=== Key Findings from the Sales Analysis ===\n")
    
    # 1. Data Quality
    print("1. Data Quality:")
    print(f"- Total records analyzed: {len(df):,}")
    print(f"- Time period covered: {df['Date'].min().strftime('%Y-%m-%d')} to {df['Date'].max().strftime('%Y-%m-%d')}")
    
    # 2. Sales Performance
    print("\n2. Sales Performance:")
    print(f"- Average daily sales: ${df['Sales'].mean():,.2f}")
    print(f"- Highest daily sales: ${df['Sales'].max():,.2f}")
    print(f"- Lowest daily sales: ${df['Sales'].min():,.2f}")
    print(f"- Total sales for the period: ${df['Sales'].sum():,.2f}")
    
    # 3. Product Performance
    best_product = product_sales['mean'].idxmax()
    print("\n3. Product Performance:")
    print(f"- Best performing product category: {best_product}")
    print(f"- Average sales for {best_product}: ${product_sales.loc[best_product, 'mean']:,.2f}")
    
    # 4. Regional Performance
    best_region = region_sales['mean'].idxmax()
    print("\n4. Regional Performance:")
    print(f"- Best performing region: {best_region}")
    print(f"- Average sales for {best_region}: ${region_sales.loc[best_region, 'mean']:,.2f}")
    
    # 5. Seasonal Patterns
    best_month = monthly_sales.idxmax()
    print("\n5. Seasonal Patterns:")
    print(f"- Highest sales month: {best_month}")
    print(f"- Sales in {best_month}: ${monthly_sales[best_month]:,.2f}")

def main():
    """Main function to run the analysis"""
    try:
        # Create sample dataset
        df = create_sample_data()
        
        # Explore and clean data
        df = explore_and_clean_data(df)
        
        # Perform basic analysis
        product_sales, region_sales, monthly_sales = perform_basic_analysis(df)
        
        # Create visualizations
        create_visualizations(df, product_sales, monthly_sales)
        
        # Print key findings
        print_key_findings(df, product_sales, region_sales, monthly_sales)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
