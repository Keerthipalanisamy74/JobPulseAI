import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="JobPulse AI",
    page_icon="📊",
    layout="wide"
)

st.title("📊 JobPulse AI")
st.subheader("Job Market Intelligence Dashboard")

col1, col2 = st.columns(2)

with col1:
    st.write("### Top Hiring Locations")
    locations = pd.read_csv("output/top_locations.csv")
    st.dataframe(locations)

with col2:
    st.write("### Top Hiring Companies")
    companies = pd.read_csv("output/top_companies.csv")
    st.dataframe(companies)

st.write("### Top Skills")
skills = pd.read_csv("output/top_skills.csv")
st.bar_chart(skills.set_index("Skill"))

st.write("### Salary Analysis")
salary = pd.read_csv("output/salary_summary.csv")
st.dataframe(salary)

st.success("JobPulse AI Running Successfully 🚀")