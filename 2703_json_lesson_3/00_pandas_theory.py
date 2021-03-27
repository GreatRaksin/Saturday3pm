import pandas as pd

my_series = pd.Series([13, 14, 15, 16, 17, 18], index=['a', 'b', 'c', 'd', 'e', 'f'])
print(my_series)

print(my_series.index)
print(my_series.values)
print(my_series[4])  # 17
# print(my_series[14]) <- низя

df = pd.DataFrame({
    'country': ['USA', 'Russia', 'Belarus', 'Montenegro'],
    'population': [150.2, 140.2, 9.6, 2.7],
    'square': [15045687, 18012591, 217400, 132000]
}, index=['US', 'RU', 'BY', 'ME'])

print(df.loc[['RU', 'US'], 'population'])  # доступ к строковой метке
# print(df.iloc[1])  # доступ по числовому значению
print(df[df.population < 10][['country', 'square']])  # булевые массивы

'''Определить плотность населения в странах'''
new_data = df['density'] = (df['population'] / df['square']) * 1000000
print(df)
