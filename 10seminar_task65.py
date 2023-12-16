# Написать EDA для датасета про пингвинов
# Необходимо:
# ● Использовать 2-3 точечных графика
# ● Применить доп измерение в точечных графиках, используя аргументы hue, size, stile
# ● Использовать PairGrid с типом графика на ваш выбор
# ● Изобразить Heatmap
# ● Использовать 2-3 гистограммы

from pandas import read_csv
import seaborn as sns
import matplotlib.pyplot as plt
from seaborn import load_dataset, scatterplot, PairGrid, displot

penguins = load_dataset("penguins")

def task1():
    scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g")
    plt.show()

def task1_1():
    scatterplot(data=penguins, x="bill_length_mm", y="bill_depth_mm")
    plt.show()

def task2():
    scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g",
                hue='sex', size='island', style='island')
    plt.show()
    
def task2_1():
    scatterplot(data=penguins, x="bill_length_mm", y="bill_depth_mm",
                hue='island', size='body_mass_g', style='sex')
    plt.show()


def task3():
    x_vars = ["bill_length_mm", "bill_depth_mm",
              "flipper_length_mm"]
    y_vars = ["body_mass_g"]
    g = PairGrid(penguins, x_vars=x_vars, y_vars=y_vars, hue='sex')
    g.map(scatterplot)
    plt.show()

def task4():
    data = penguins.pivot_table(index='species', columns='sex',
                                values='body_mass_g')
    sns.heatmap(data)
    plt.xlabel('Пол пингвина', size=14)
    plt.ylabel('Вид пингвина', size=14)
    plt.show()

def task5():
    penguins['flipper_length_mm'].hist(bins=10)
    plt.xlabel('Длина плавника (мм)', size=14)
    plt.show()

def task5_1():
    penguins['body_mass_g'].hist(bins=10)
    plt.xlabel('Масса пингвина (гр)', size=14)
    plt.show()

# print(penguins.info())
# task1()
# task1_1()
# task2()
# task2_1()
# task3()
# task4()
task5()
task5_1()