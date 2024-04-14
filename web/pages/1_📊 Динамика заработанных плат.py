import streamlit as st
from data import load_data
import plotly.express as px

path = '\web\.env'
query = '''select name, year, mean_salary
from data.salary s
inner join data.ref_salary rs on rs.id = s.economic_id'''
df = load_data(path, query)
st.dataframe(df)
st.markdown('[Source](https://rosstat.gov.ru/labor_market_employment_salaries)')

st.line_chart(df, x="year", y="mean_salary", color="name")