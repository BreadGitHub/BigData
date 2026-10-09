import pandas as pd
import numpy as np

# Продажи
sales = pd.DataFrame({
    'OrderID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Product': ['Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone',
            'Laptop', 'Tablet', 'Phone', 'Laptop', 'Tablet'],
    'Quantity': [1, 2, 1, 3, 1, 2, 1, 4, 1, 2],
    'Price': [50000, 30000, 20000, 50000, np.nan,
            50000, 20000, 30000, 50000, np.nan],
    'Region': ['Moscow', 'SPb', 'Kazan', 'Moscow', 'SPb',
            'Kazan', np.nan, 'SPb', 'Moscow', 'Kazan']
})

# Информация о товарах
products = pd.DataFrame({
    'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Accessories'],
    'Weight_kg': [2.5, 0.2, 0.5, 3.0]
})

# Найти минимальную и максимальную цену для каждого продукта
def get_min_max_each_product(dataframe):
    print(dataframe.groupby('Product')['Price'].agg(['min', 'max']))

# Посчитать количество заказов в каждом регионе (.value_counts())
def count_orders_per_region(dataframe):
    print(dataframe['Region'].value_counts())

# Заполнить пропуски в столбце Region значением 'Unknown'
def fill_unknown_column_region(dataframe):
    dataframe2 = dataframe.copy()
    dataframe2['Region'] = dataframe2['Region'].fillna('Unknown')
    print(dataframe2)

# Отсортировать таблицу по Region , затем по Price
def sort_by_region_then_price(dataframe):
    print(dataframe.sort_values(by=['Region', 'Price']))

# Выполнить left join таблиц sales и products
def left_join_for_tables(dataframe_sales, dataframe_products):
    print(pd.merge(dataframe_sales, dataframe_products, on='Product', how='left'))
    
print('Задание 1')
get_min_max_each_product(sales)

print('Задание 2')
count_orders_per_region(sales)

print('Задание 3')
fill_unknown_column_region(sales)

print('Задание 4')
sort_by_region_then_price(sales)

print('Задание 5')
left_join_for_tables(sales, products)