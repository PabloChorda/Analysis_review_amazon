# Importar bibliotecas
import pandas as pd

# Ruta del dataset (ajusta si es necesario)
dataset_path = '/Users/bigsur/Desktop/SentimentAnalysisAmazon/data/amazon_reviews.csv'

# Cargar el archivo CSV
df = pd.read_csv(dataset_path)

# Exploración inicial del dataset
print("Primeras filas del dataset:")
print(df.head())

print("\nInformación del dataset:")
print(df.info())

print("\nEstadísticas descriptivas del dataset:")
print(df.describe())

# Ver columnas
print("\nColumnas del dataset:")
print(df.columns)

# Mostrar las primeras filas
print("Primeras filas del dataset:")
print(df.head())

# Resumen del dataset
print("\nResumen del dataset:")
print(df.info())

# Filtrar columnas relevantes
if 'reviewText' in df.columns and 'overall' in df.columns:
    df = df[['reviewText', 'overall']]
    print("\nColumnas seleccionadas:")
    print(df.head())
else:
    print("Las columnas 'reviewText' y 'overall' no están disponibles.")
