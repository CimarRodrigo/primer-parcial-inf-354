import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('./Student_performance_data _.csv')

# Seleccionamos las columnas que nos interesan
columas = ['Age', 'StudyTimeWeekly', 'GPA']
data_elegida = data[columas].dropna()

for col in columas:
    if col == 'GPA':
        continue
    plt.figure(figsize=(10, 5))
    sns.scatterplot(x=data_elegida[col], y=data_elegida['GPA'], color='green')
    plt.title(f'{col} vs GPA')
    plt.xlabel(col)
    plt.ylabel('GPA')
    plt.show()


plt.figure(figsize=(10, 5))
sns.heatmap(data=data_elegida.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Mapa de calor: correlación entre las variables')
plt.show()

