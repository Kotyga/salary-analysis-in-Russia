from dotenv import load_dotenv
import os
import psycopg2
import pandas as pd

# Загрузка переменных среды из файла .env
load_dotenv()

# Параметры подключения к базе данных
conn = psycopg2.connect(
    dbname=os.getenv("DATABASE_NAME"),
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
    host=os.getenv("HOST"),
    port=os.getenv("PORT")
)

# Создание объекта курсора
cur = conn.cursor()

# Пример выполнения запроса
cur.execute("SELECT * FROM data.salary")

# Получение результатов запроса
rows = cur.fetchall()

# загружаем в датафрейм
df = pd.DataFrame(rows, columns=[desc[0] for desc in cur.description])


print(df)
# Закрытие курсора
cur.close()

# Закрытие соединения с базой данных
conn.close()