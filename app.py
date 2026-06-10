import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="MF Analytics Dashboard", page_icon="📈", layout="wide")

# Dashboard Title
st.title("📈 Bluestock Mutual Fund Analytics")
st.markdown("Interactive dashboard to analyze Mutual Fund performance and custom scorecards.")

# Load Scorecard Data
@st.cache_data
def load_data():
    return pd.read_csv('fund_scorecard.csv')

try:
    df = load_data()
    
    # Sidebar Filters
    st.sidebar.header("🔍 Filter Options")
    
    # Category Filter
    categories = df['category'].unique()
    selected_category = st.sidebar.selectbox("Select Category", ["All Categories"] + list(categories))
    
    # Filter Logic
    if selected_category != "All Categories":
        filtered_df = df[df['category'] == selected_category]
    else:
        filtered_df = df
        
    # Top Level Metrics
    st.subheader("📊 Market Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Funds", len(filtered_df))
    col2.metric("Highest Composite Score", f"{filtered_df['composite_score'].max():.2f}/100")
    col3.metric("Avg 3Y Return", f"{filtered_df['cagr_3y'].mean() * 100:.2f}%")
    
    # Data Table
    st.subheader("🏆 Top Ranked Funds")
    
    # Format columns for better display
    display_cols = ['amfi_code', 'scheme_name', 'category', 'cagr_3y', 'sharpe_ratio', 'alpha', 'composite_score']
    st.dataframe(
        filtered_df[display_cols].sort_values('composite_score', ascending=False),
        width="stretch",
        hide_index=True
    )
    
except FileNotFoundError:
    st.error("⚠️ 'fund_scorecard.csv' file not found. Please ensure Day 4 script was run successfully!")