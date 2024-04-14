import psycopg2
import pandas as pd
import streamlit as st

PORT=5432
@st.cache_data
def load_data(sql_txt):
    conn = psycopg2.connect(
        dbname='salary-project-db',
        user='guest',
        password='BnC0ojgWq6JT',
        host='ep-floral-hall-a2pqbcyz.eu-central-1.aws.neon.tech',
        port=5432
    )
    cur = conn.cursor()
    cur.execute(sql_txt)
    rows = cur.fetchall()
    df = pd.DataFrame(rows, columns=[desc[0] for desc in cur.description])
    cur.close()
    conn.close()
    return df

@st.cache_data
def inflation(salary, inflation_idx):
    inflation_idx /= 100
    return salary * (salary / (salary * (1 + inflation_idx)))