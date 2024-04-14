from dotenv import load_dotenv
import os
import psycopg2
import pandas as pd
import streamlit as st


@st.cache_data
def load_data(env_path, sql_txt):
    load_dotenv(env_path)
    conn = psycopg2.connect(
        dbname=os.getenv("DATABASE_NAME"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        host=os.getenv("HOST"),
        port=os.getenv("PORT")
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