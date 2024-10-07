import pandas as pd
import matplotlib.pyplot as plt

def calcular_percentil(data, percentil):
    if not 0 <= percentil <= 100:
        return "El percentil debe estar entre 0 y 100"

    data_ordenada = sorted(data)
    n = len(data_ordenada)

    posicion = (percentil / 100) * (n - 1)
    
    parte_entera = int(posicion)
    decimal = posicion - parte_entera

    if decimal == 0:
        return data[parte_entera]
    else:
        siguiente = parte_entera + 1

        return data_ordenada[siguiente] 


percentil = int(input("Ingrese el percentil que desea calcular: "))
data = pd.read_csv('./Student_performance_data _.csv')

# Percentiles
# percentiles = data.describe(percentiles=[0.25, 0.5, 0.75])
# print(percentiles['Age'])


for i in data.columns:
    print(f"Percentil {percentil} de {i}: ", calcular_percentil(data[i], percentil))
    print(f"Cuartil 1 de {i}: ", calcular_percentil(data[i], 25))
    print(f"Cuartil 2 de {i}: ", calcular_percentil(data[i], 50))
    print(f"Cuartil 3 de {i}: ", calcular_percentil(data[i], 75))
    print()


# Histograma

for i in data.columns:
    plt.hist(data[i], bins=40)
    plt.title(f"Histograma de {i}")
    plt.show()
