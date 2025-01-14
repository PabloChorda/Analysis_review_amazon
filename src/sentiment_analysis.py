# Importar bibliotecas
import pandas as pd

# Ruta del dataset (ajusta si es necesario)
dataset_path = '/Users/bigsur/Desktop/SentimentAnalysisAmazon/data/amazon_reviews.csv'

# Cargar el archivo CSV
try:
    df = pd.read_csv(dataset_path)
    print("\nDataset cargado exitosamente.")
except FileNotFoundError:
    print("\nError: El archivo no se encontró en la ruta especificada.")
    exit()

# --- Exploración inicial del dataset ---
print("\n--- Exploración inicial ---")
print("Primeras filas del dataset:")
print(df.head())

print("\nInformación del dataset:")
print(df.info())

print("\nEstadísticas descriptivas:")
print(df.describe())

print("\nValores nulos por columna:")
print(df.isnull().sum())

print("\nNúmero de filas duplicadas:")
print(df.duplicated().sum())

# --- Filtrar y limpiar el dataset ---
print("\n--- Filtrado y limpieza ---")
if 'reviews.text' in df.columns and 'reviews.rating' in df.columns:
    df = df[['reviews.text', 'reviews.rating']]
    print("\nColumnas seleccionadas (reviews.text y reviews.rating):")
    print(df.head())
else:
    print("\nError: Las columnas 'reviews.text' y 'reviews.rating' no están disponibles en el dataset.")
    exit()

# Eliminar valores nulos
df = df.dropna(subset=['reviews.text', 'reviews.rating'])
print(f"\nDataset después de eliminar valores nulos: {df.shape[0]} filas restantes.")

# Mapear puntuaciones a etiquetas de sentimiento
def map_sentiment(rating):
    if rating >= 4:
        return 'positivo'
    elif rating == 3:
        return 'neutral'
    else:
        return 'negativo'

df['sentiment'] = df['reviews.rating'].apply(map_sentiment)
print("\nEjemplo de etiquetas asignadas:")
print(df[['reviews.rating', 'sentiment']].head())

# Guardar dataset limpio
output_path = '/Users/bigsur/Desktop/SentimentAnalysisAmazon/data/cleaned_sentiment_reviews.csv'
df.to_csv(output_path, index=False)
print(f"\nDataset limpio guardado en: {output_path}")
