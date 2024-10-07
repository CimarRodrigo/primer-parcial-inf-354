import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, KBinsDiscretizer, Normalizer

# Abrir el archivo CSV existente
data = pd.read_csv("../ejercicio_2/Student_performance_data _.csv")

# Mostrar el DataFrame original
print("Contenido del DataFrame original:")
print(data)

# Paso 1: Label Encoding para columnas categóricas
label_encoder = LabelEncoder()
data['Gender'] = label_encoder.fit_transform(data['Gender'])
data['Ethnicity'] = label_encoder.fit_transform(data['Ethnicity'])
data['Tutoring'] = label_encoder.fit_transform(data['Tutoring'])
data['ParentalSupport'] = label_encoder.fit_transform(data['ParentalSupport'])

# Mostrar el resultado del Label Encoding
print("\nContenido después de Label Encoding:")
print(data)

# Paso 2: One-Hot Encoding (aplicado a columnas categóricas)
data = pd.get_dummies(data, columns=['Ethnicity', 'Tutoring', 'ParentalSupport'])

# Mostrar el resultado del One-Hot Encoding
print("\nContenido después de One-Hot Encoding:")
print(data)

# Paso 3: Discretización (para la columna StudyTimeWeekly)
discretizer = KBinsDiscretizer(n_bins=4, encode='ordinal', strategy='uniform')
data['StudyTimeWeekly_binned'] = discretizer.fit_transform(data[['StudyTimeWeekly']])

# Mostrar el resultado de la Discretización
print("\nContenido después de Discretización:")
print(data)

# Paso 4: Normalización usando Normalizer
normalizer = Normalizer()
data[['Age', 'StudyTimeWeekly', 'GPA']] = normalizer.fit_transform(data[['Age', 'StudyTimeWeekly', 'GPA']])

# Mostrar el resultado de la Normalización
print("\nContenido después de Normalización:")
print(data)
