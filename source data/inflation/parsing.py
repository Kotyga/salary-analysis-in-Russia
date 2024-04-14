import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://уровень-инфляции.рф/таблицы-инфляции"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
names = ['Год','Янв','Фев','Мар','Апр','Май','Июн','Июл','Авг','Сен','Окт','Ноя','Дек','Всего']
tables = soup.find_all("table", class_="table table-hover table-sm")
for idx, table in enumerate(tables):
    # Создаем пустой DataFrame
    df = pd.DataFrame(columns=names)
    
    rows = table.find_all("tr")
    for row in rows:
        columns = row.find_all("td")
        data = [[column.get_text()] for column in columns]
        d = pd.DataFrame(dict(zip(names, data)))
        df = pd.concat([df, d], ignore_index=True)
        
    # Сохраняем DataFrame в CSV файл
    df.to_csv(f"./source data/inflation/table_{idx}.csv", index=False)