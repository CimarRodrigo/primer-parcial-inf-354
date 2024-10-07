import pandas as pd
def penalizacion_l1(pesos, alpha):
    return alpha * sum(abs(peso) for peso in pesos)

def penalizacion_l2(pesos, alpha):
    return alpha * sum(peso ** 2 for peso in pesos)

def normalizar(X):
    # Calcular la media y la desviación estándar de cada columna
    medias = []
    desviaciones_estandar = []
    
    # Transponer X para facilitar el cálculo de media y desviación estándar por columna
    matriz_transpuesta = list(zip(*X))

    for columna in matriz_transpuesta:
        media = sum(columna) / len(columna)
        medias.append(media)
        
        varianza = sum((x - media) ** 2 for x in columna) / len(columna)
        desviacion_estandar = varianza ** 0.5
        desviaciones_estandar.append(desviacion_estandar)
    
    # Normalizar los datos
    X_normalizado = []
    
    for fila in X:
        fila_normalizada = [(fila[j] - medias[j]) / desviaciones_estandar[j] if desviaciones_estandar[j] != 0 else 0 for j in range(len(fila))]
        X_normalizado.append(fila_normalizada)
    
    return X_normalizado

def regresion_l1(X, y, alpha, tasa_aprendizaje, epocas):
    # Inicializar los pesos (coeficientes) y el sesgo (bias)
    n_muestras = len(X)
    n_caracteristicas = len(X[0])
    w = [0.0] * n_caracteristicas  
    b = 0.0  
    
    for epoca in range(epocas):
        # Predicción
        y_pred = [sum(X[i][j] * w[j] for j in range(n_caracteristicas)) + b for i in range(n_muestras)]
        
        # Calcular gradientes
        dw = [0.0] * n_caracteristicas
        db = 0.0
        
        for i in range(n_muestras):
            error = y_pred[i] - y[i]
            for j in range(n_caracteristicas):
                dw[j] += error * X[i][j]  # Error * entrada
            db += error  # Sumar el error
        
        # Promediar los gradientes
        dw = [d / n_muestras for d in dw]
        db /= n_muestras
        
        # Agregar penalización L1 a los gradientes
        for j in range(n_caracteristicas):
            # Actualizar con la penalización L1
            if w[j] > 0:
                dw[j] += alpha  # Ajustar por la penalización L1 positiva
            elif w[j] < 0:
                dw[j] -= alpha  # Ajustar por la penalización L1 negativa
        
        # Actualizar pesos y sesgo
        for j in range(n_caracteristicas):
            w[j] -= tasa_aprendizaje * dw[j]
        b -= tasa_aprendizaje * db
    
    return w, b

def regresion_l2(X, y, alpha, tasa_aprendizaje, epocas):
    # Inicializar los pesos (coeficientes) y el sesgo (bias)
    n_muestras = len(X)
    n_caracteristicas = len(X[0])
    
    w = [0.0] * n_caracteristicas
    b = 0.0

    for epoca in range(epocas):
        # Gradientes acumulados para los pesos y el sesgo
        dw = [0.0] * n_caracteristicas
        db = 0.0

        # Predicción 
        y_pred = [sum(X[i][j] * w[j] for j in range(n_caracteristicas)) + b for i in range(n_muestras)]

        for i in range(n_muestras):
            
            # Calcular el error (y_pred - y_real)
            error = y_pred[i] - y[i]
            
            # Actualizar los gradientes acumulados para cada peso
            for j in range(n_caracteristicas):
                dw[j] += (error * X[i][j]) / n_muestras
            
            # Actualizar el gradiente acumulado para el sesgo
            db += error / n_muestras
        
        # Actualizar los pesos y el sesgo con penalización L2
        for j in range(n_caracteristicas):
            # Gradiente descendente con penalización L2
            w[j] = w[j] - tasa_aprendizaje * (dw[j] + 2 * alpha * w[j])
        
        # Actualizar el sesgo (bias)
        b = b - tasa_aprendizaje * db

    return w, b


# Datos de entrenamiento
# X = pd.read_csv('../ejercicio_2/Student_performance_data _.csv')
# y = X['GradeClass'].values

# # Eliminar la columna de la variable objetivo
# X = X.drop('GradeClass', axis=1).values

X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = [1, 2, 3]

# Normalizar los Datos
X_normalizado = normalizar(X)

# Entrenar el modelo
alpha = 0.01
tasa_aprendizaje = 0.01
epocas = 1000
coef_l1, sesgo_l1 = regresion_l1(X_normalizado, y, alpha, tasa_aprendizaje, epocas)
coef_l2, sesgo_l2 = regresion_l2(X_normalizado, y, alpha, tasa_aprendizaje, epocas)
print("Coeficientes L1:", coef_l1)
# print("Sesgo:", sesgo)
print("Coeficientes L2:", coef_l2)
# print("Sesgo Ridge:", sesgo2)


