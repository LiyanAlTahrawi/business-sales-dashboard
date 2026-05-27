import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(
    page_title="Business Sales Intelligence Dashboard",
    page_icon="📊",
    layout="wide"
)

model = joblib.load("advanced_sales_prediction_model.pkl")
model_columns = joblib.load("model_columns.pkl")
df = pd.read_csv("cleaned_superstore_sales.csv")
feature_importance = pd.read_csv("feature_importance.csv")

df["order_date"] = pd.to_datetime(df["order_date"])
df["ship_date"] = pd.to_datetime(df["ship_date"])

st.title("Business Sales Intelligence Dashboard")
st.write("Interactive business dashboard with sales analysis and machine learning sales prediction.")

st.sidebar.header("Business Filters")

selected_years = st.sidebar.multiselect(
    "Year",
    sorted(df["year"].unique()),
    default=sorted(df["year"].unique())
)

selected_regions = st.sidebar.multiselect(
    "Region",
    sorted(df["region"].unique()),
    default=sorted(df["region"].unique())
)

selected_categories = st.sidebar.multiselect(
    "Category",
    sorted(df["category"].unique()),
    default=sorted(df["category"].unique())
)

selected_segments = st.sidebar.multiselect(
    "Segment",
    sorted(df["segment"].unique()),
    default=sorted(df["segment"].unique())
)

filtered_df = df[
    (df["year"].isin(selected_years)) &
    (df["region"].isin(selected_regions)) &
    (df["category"].isin(selected_categories)) &
    (df["segment"].isin(selected_segments))
]

st.subheader("Executive Summary")

total_sales = filtered_df["sales"].sum()
total_profit = filtered_df["profit"].sum()
total_orders = filtered_df["order_id"].nunique()
avg_order_value = total_sales / total_orders if total_orders != 0 else 0
profit_margin = (total_profit / total_sales) * 100 if total_sales != 0 else 0

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Profit Margin", f"{profit_margin:.2f}%")
col4.metric("Total Orders", f"{total_orders:,}")
col5.metric("Avg Order Value", f"${avg_order_value:,.2f}")

st.divider()

st.subheader("Sales and Profit Trends")

monthly_trend = filtered_df.groupby(["year", "month"])[["sales", "profit"]].sum().reset_index()
monthly_trend["date"] = pd.to_datetime(monthly_trend[["year", "month"]].assign(day=1))
monthly_trend = monthly_trend.sort_values("date")

col1, col2 = st.columns(2)

with col1:
    st.write("Monthly Sales Trend")
    st.line_chart(monthly_trend.set_index("date")["sales"])

with col2:
    st.write("Monthly Profit Trend")
    st.line_chart(monthly_trend.set_index("date")["profit"])

st.divider()

st.subheader("Business Performance Breakdown")

col1, col2 = st.columns(2)

with col1:
    sales_by_category = filtered_df.groupby("category")["sales"].sum().sort_values(ascending=False)
    st.write("Sales by Category")
    st.bar_chart(sales_by_category)

with col2:
    profit_by_category = filtered_df.groupby("category")["profit"].sum().sort_values(ascending=False)
    st.write("Profit by Category")
    st.bar_chart(profit_by_category)

col3, col4 = st.columns(2)

with col3:
    sales_by_region = filtered_df.groupby("region")["sales"].sum().sort_values(ascending=False)
    st.write("Sales by Region")
    st.bar_chart(sales_by_region)

with col4:
    profit_by_region = filtered_df.groupby("region")["profit"].sum().sort_values(ascending=False)
    st.write("Profit by Region")
    st.bar_chart(profit_by_region)

st.divider()

st.subheader("Product-Level Insights")

col1, col2 = st.columns(2)

with col1:
    top_products = filtered_df.groupby("product_name")["sales"].sum().sort_values(ascending=False).head(10)
    st.write("Top 10 Products by Sales")
    st.bar_chart(top_products)

with col2:
    worst_profit_products = filtered_df.groupby("product_name")["profit"].sum().sort_values(ascending=True).head(10)
    st.write("Worst 10 Products by Profit")
    st.bar_chart(worst_profit_products)

st.divider()

st.subheader("Machine Learning Sales Prediction Simulator")

st.write("Use this section to simulate expected sales based on business conditions.")

col1, col2, col3 = st.columns(3)

with col1:
    input_year = st.number_input("Year", min_value=2020, max_value=2035, value=2025)
    input_month = st.selectbox("Month", list(range(1, 13)))
    input_quantity = st.number_input("Quantity", min_value=1, max_value=100, value=3)

with col2:
    input_discount = st.slider("Discount", min_value=0.0, max_value=0.9, value=0.1, step=0.01)
    input_profit = st.number_input("Expected Profit", min_value=-5000.0, max_value=10000.0, value=50.0)
    input_region = st.selectbox("Region", sorted(df["region"].unique()))

with col3:
    input_category = st.selectbox("Category", sorted(df["category"].unique()))
    input_sub_category = st.selectbox("Sub-Category", sorted(df["sub_category"].unique()))
    input_segment = st.selectbox("Segment", sorted(df["segment"].unique()))
    input_ship_mode = st.selectbox("Ship Mode", sorted(df["ship_mode"].unique()))

input_data = pd.DataFrame({
    "profit": [input_profit],
    "quantity": [input_quantity],
    "discount": [input_discount],
    "year": [input_year],
    "month": [input_month],
    "category": [input_category],
    "sub_category": [input_sub_category],
    "region": [input_region],
    "segment": [input_segment],
    "ship_mode": [input_ship_mode]
})

input_encoded = pd.get_dummies(input_data)
input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)

if st.button("Predict Sales"):
    predicted_sales = model.predict(input_encoded)[0]

    st.success(f"Predicted Sales: ${predicted_sales:,.2f}")

    if input_discount >= 0.3 and input_profit < 0:
        st.error("Risk Level: High. Discount is high and expected profit is negative.")
        st.write("Recommendation: Reduce discount or review product pricing before scaling sales.")
    elif input_discount >= 0.3:
        st.warning("Risk Level: Medium. High discount may reduce profitability.")
        st.write("Recommendation: Monitor profit margin carefully.")
    elif predicted_sales > filtered_df["sales"].mean():
        st.success("Business Signal: Strong expected sales compared to the current average.")
        st.write("Recommendation: Consider increasing stock availability for this scenario.")
    else:
        st.info("Business Signal: Normal sales expectation.")
        st.write("Recommendation: Continue monitoring performance by region and category.")

st.divider()

st.subheader("Model Feature Importance")

top_features = feature_importance.head(15).set_index("Feature")
st.bar_chart(top_features["Importance"])

st.divider()

st.subheader("Filtered Data Preview")
st.dataframe(filtered_df.head(100))