import pandas as pd
from pandas import Series, DataFrame
import os
import matplotlib.pyplot as plt


df = pd.read_csv(r'C:/Users/morfo/PycharmProjects/proekt/data_lab2/yob1955.txt', names=('имя', 'пол', 'кол-во'))
df_f = df[df['пол'] == 'F']
df_m = df[df['пол'] == 'M']
Total_F = df_f['кол-во'].sum()
Total_M = df_m['кол-во'].sum()
print("....................\nзадача 1\n1955 год: \n")
print ("F sum:",Total_F)
print ("M sum:",Total_M)
print("....................")

print("....................\nзадача 2\n")
i = 1881
df = pd.read_csv(r'C:/Users/morfo/PycharmProjects/proekt/data_lab2/yob'+ str(1880) + '.txt', names=('имя', 'пол', 'кол-во'))
df['год'] = str(1880)
while i < 2011:
    df2 = pd.read_csv(r'C:/Users/morfo/PycharmProjects/proekt/data_lab2/yob'+ str(i) + '.txt', names=('имя', 'пол', 'кол-во'))
    df2['год'] = str(i)
    df = pd.concat([df, df2])
    i = i + 1
print(df)
dfdf = df.copy()

print("....................\nзадача 3\n График\n")

i = 1880
col = ['год', 'кол-воF', 'кол-воM']
df_new = pd.DataFrame(columns=col)
while i < 2011:
    df_x = df[df['год'] == str(i)]
    df_f = df_x[df_x['пол'] == 'F']
    df_m = df_x[df_x['пол'] == 'M']
    Total_F = df_f['кол-во'].sum()
    Total_M = df_m['кол-во'].sum()
    df_new.loc[len(df_new)]=[str(i),Total_F, Total_M]
    i = i + 1
    
df_new.plot(x='год', y=['кол-воF', 'кол-воM'])
plt.show()

print("....................\nзадача 4\n")
df.drop('год', axis=1, inplace=True)
df = df.groupby('имя').agg({'кол-во':'sum'}).reset_index()
Total_All = (df['кол-во'].sum())
print("Всего родилось с 1880 по 2010: ",Total_All)

for index, row in df.iterrows():
    df['пропорция'] = df['кол-во'] / Total_All

print(df)

print("....................\nзадача 5\n")

df_5 = df.loc[df['имя'] == 'Johny']
df_5 = pd.concat([df_5, df.loc[df['имя'] == 'Natalie']])
df_5 = pd.concat([df_5,df.loc[df['имя'] == 'Bob']])
df_5 = pd.concat([df_5,df.loc[df['имя'] == 'Danil']])

print(df_5)
df_5.plot(x='имя', y='кол-во')
plt.show()
df_5.plot(x='имя', y='пропорция')
plt.show()

print("....................\nзадача 6\n Самые популярные имена по годам:")
i = 1880
dfdf = dfdf.sort_values(by='кол-во')

while i < 2011:
    df_6 = dfdf.loc[dfdf['год'] == str(i)]
    print(df_6.iloc[-1].tolist())
    i = i + 1
    print("-----")
KEKW
