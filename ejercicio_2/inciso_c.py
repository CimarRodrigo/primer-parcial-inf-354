import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


data = pd.read_csv('./Student_performance_data _.csv')

columnas_elegidas = ['Age', 'StudyTimeWeekly', 'GPA']

data = data[columnas_elegidas].dropna()

for col in columnas_elegidas:
    media = data[col].mean()
    mediana = data[col].median()
    moda = data[col].mode()[0]

    print(f'Columna: {col}')
    print(f'Media: {media}')
    print(f'Mediana: {mediana}')
    print(f'Moda: {moda}')

    print()


plt.figure(figsize=(10, 5))
sns.boxplot(data=data)

plt.title('Diagrama caja y bigotes')
plt.xlabel('Columnas')
plt.ylabel('Valores')
plt.show()
