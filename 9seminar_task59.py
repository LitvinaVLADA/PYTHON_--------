# 1. Проверить есть ли в файле пустые значения
# 2. Показать median_house_value где median_income < 2
# 3. Показать данные в первых 2 столбцах
# 4. Выбрать данные где housing_median_age < 20 и median_house_value > 70000

from pandas import read_csv
data = read_csv('california_housing_test.csv')

print('Проверка на пустые значения в файле:')
print(data.isnull().sum())

print('Проверка median_house_value где median_income < 2:')
res = data[data['median_income'] < 2]['median_house_value']
print(res)

print('Вывод первых двух столбцов')
two_col = data.iloc[:, :2]
print(two_col)

print('Проверка housing_median_age < 20 и median_house_value > 70000:')
res = data[(data["housing_median_age"] < 20) & (data["median_house_value"] > 70000)]
print(res)