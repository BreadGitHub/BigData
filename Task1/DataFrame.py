import pandas as pd
import numpy as np

data = {
    'ID': range(1, 11),
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva',
            'Frank', 'Grace', 'Helen', 'Ivan', 'Julia'],
    'Age': [23, 35, 29, 40, 28, 45, 32, 27, 38, 31],
    'City': ['Moscow', 'SPb', 'Moscow', 'Kazan', 'SPb',
            'Moscow', 'SPb', 'Kazan', 'Moscow', 'SPb'],
    'Salary': [50000, 70000, 60000, 80000, 55000,
            90000, 65000, 58000, 75000, 62000]
}

df = pd.DataFrame(data)

# Вывести последние 3 строки DataFrame
def show_last_three_rows(dataframe):
    print(dataframe.tail(3))

# Выбрать строки с индексами 2, 4, 6 используя .iloc[]
def select_rows(dataframe):
    print(dataframe.iloc[[2, 4, 6]])

# Выбрать строки, где City == 'Moscow'
def rows_where_moscow(dataframe):
    print(dataframe[dataframe['City'] == 'Moscow'])

# Найти максимальное значение Age
def get_max_age(dataframe):
    print(dataframe['Age'].max())

# Создать столбец Age_Category : если Age < 30 → "Young", иначе → "Adult"
def add_column_age_category(dataframe):
    dataframe_2 = dataframe.copy()
    dataframe_2['Age_Category'] = np.where(dataframe_2['Age'] < 30, 'Young', 'Adult')
    print(dataframe_2)

print('Задание 1')
show_last_three_rows(df)

print('Задание 2')
select_rows(df)

print('Задание 3')
rows_where_moscow(df)

print('Задание 4')
get_max_age(df)

print('Задание 5')
add_column_age_category(df)