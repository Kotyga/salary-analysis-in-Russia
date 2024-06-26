import streamlit as st
from data import load_data, inflation
import plotly.express as px

query = '''select name, year, mean_salary
from data.salary s
inner join data.ref_salary rs on rs.id = s.economic_id'''
df = load_data(query)
st.title('''Таблица зарплат по отраслям с 2000г.''')
st.dataframe(df)
st.markdown('[Source](https://rosstat.gov.ru/labor_market_employment_salaries)')

st.line_chart(df, x="year", y="mean_salary", color="name")

query0 = 'SELECT * FROM data.inflation_data_0'
query1 = '''select name, s.year, mean_salary, total
from data.salary s
inner join data.ref_salary rs on rs.id = s.economic_id
inner join data.inflation_data_0 id0 on id0.year = s.year'''
df11 = load_data(query0)
df1 = load_data(query1)
st.title('''Таблица уровня инфляции по месяцам в годовом исчислении''')
st.write('''Коэффициент инфляции в годовом исчислении,
         представленный в таблице ниже, рассчитывается как сумма коэффициентов инфляции 
         за 12 месяцев, включая выбранный. Такой способ позволяет оценить динамику изменения 
         уровня инфляции в целом, сглаживая сезонные отклонения.)''')
st.dataframe(df11)
st.markdown('[Source](https://уровень-инфляции.рф/таблицы-инфляции)')
df1['salary_gen'] = df1.apply(lambda row: inflation(row['mean_salary'], row['total']), axis=1)
st.line_chart(df1, x='year', y='salary_gen', color="name")

query0 = 'SELECT * FROM data.inflation_data_1'
query1 = '''select name, s.year, mean_salary, total
from data.salary s
inner join data.ref_salary rs on rs.id = s.economic_id
inner join data.inflation_data_1 id0 on id0.year = s.year'''
df11 = load_data(query0)
df1 = load_data(query1)
st.title('''Таблица уровня инфляции по месяцам в годовом исчислении''')
st.write('''В таблице ниже представлен уровень инфляции 
         за каждый месяц в отдельности, с первое по последнее число месяца.''')
st.dataframe(df11)
st.markdown('[Source](https://уровень-инфляции.рф/таблицы-инфляции)')
df1['salary_rel'] = df1.apply(lambda row: inflation(row['mean_salary'], row['total']), axis=1)
st.line_chart(df1, x='year', y='salary_rel', color="name")

choice = st.selectbox(
    'Выберите отрасль:',
    ('Финансовая деятельность', 'Образование', 'Здравоохранение и предоставление социальных услуг')
)

# Строим график
fig = px.line()
d = df[df['name']==choice]
dd = df1[df1['name']==choice]
# Строим график
fig = px.line(d, x="year", y="mean_salary")
fig.add_scatter(x=dd["year"], y=dd["salary_rel"], mode="lines")

# Отображаем график
st.plotly_chart(fig)