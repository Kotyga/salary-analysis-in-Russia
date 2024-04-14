import streamlit as st
from data import load_data, inflation

query0 = 'SELECT * FROM data.inflation_data_1'
query1 = '''select name, s.year, mean_salary, total
from data.salary s
inner join data.ref_salary rs on rs.id = s.economic_id
inner join data.inflation_data_1 id0 on id0.year = s.year'''
df = load_data(query0)
df1 = load_data(query1)
st.title('''Таблица уровня инфляции по месяцам в годовом исчислении''')
st.write('''В таблице ниже представлен уровень инфляции 
         за каждый месяц в отдельности, с первое по последнее число месяца.''')
st.dataframe(df)
st.markdown('[Source](https://уровень-инфляции.рф/таблицы-инфляции)')
df1['salary_rel'] = df1.apply(lambda row: inflation(row['mean_salary'], row['total']), axis=1)
st.line_chart(df1, x='year', y='salary_rel', color="name")