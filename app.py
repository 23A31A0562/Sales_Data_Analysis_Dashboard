import streamlit as st
import pandas as pd
from sales_analyzer.data_loader import DataLoader
from sales_analyzer.data_cleaner import DataCleaner
from sales_analyzer.analyzer import SalesAnalyzer
from sales_analyzer.visualizer import Visualizer

st.set_page_config(page_title="Sales Data Analysis Dashboard", layout="wide")

st.title("📊 Sales Data Analysis Dashboard")

uploaded_file = st.file_uploader("Upload Sales CSV File", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df["order_date"] = pd.to_datetime(df["order_date"])

    cleaner = DataCleaner()
    df = cleaner.clean(df)

    analyzer = SalesAnalyzer(df)
    summary = analyzer.basic_stats()
    monthly = analyzer.monthly_trends()
    category = analyzer.sales_by_category()

    st.subheader("📌 Key Metrics")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Sales", f"${summary['total_sales']:.2f}")
    col2.metric("Avg Order", f"${summary['average_order']:.2f}")
    col3.metric("Orders", summary["total_orders"])
    col4.metric("Customers", summary["unique_customers"])

    st.subheader("📈 Monthly Sales Trend")
    st.line_chart(monthly)

    st.subheader("📊 Sales by Category")
    st.bar_chart(category)
