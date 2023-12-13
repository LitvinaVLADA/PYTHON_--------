# 1. Прочесть с помощью pandas файл california_housing_test.csv, который находится в папке sample_data
# 2. Посмотреть сколько в нем строк и столбцов
# 3. Определить какой тип данных имеют столбцы


from pandas import read_csv

data = read_csv('california_housing_test.csv')
print(type(data))  # <class 'pandas.core.frame.DataFrame'>
# print(data)
# print(data.dtypes)

print(data.shape)
print(data.info())
print(data.describe())