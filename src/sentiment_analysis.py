# Importar bibliotecas
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

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

# --- Preprocesamiento de texto ---
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Descargar stopwords si es necesario
import nltk
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def clean_text(text):
    # Eliminar caracteres especiales, números y convertir a minúsculas
    text = re.sub(r'[^a-zA-Z]', ' ', text).lower()
    # Tokenización y eliminación de stopwords
    tokens = text.split()
    tokens = [stemmer.stem(word) for word in tokens if word not in stop_words]
    return ' '.join(tokens)

df['cleaned_text'] = df['reviews.text'].apply(clean_text)
print("\nTexto limpio (ejemplo):")
print(df[['reviews.text', 'cleaned_text']].head())

# Guardar dataset limpio
output_path = '/Users/bigsur/Desktop/SentimentAnalysisAmazon/data/cleaned_sentiment_reviews.csv'
df.to_csv(output_path, index=False)
print(f"\nDataset limpio guardado en: {output_path}")

# --- Vectorización y división de datos ---
# Configurar el vectorizador TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)  # Limitamos a 5000 palabras más frecuentes

# Convertir el texto limpio a una representación numérica
X = vectorizer.fit_transform(df['cleaned_text']).toarray()
y = df['sentiment']

# Verificar la dimensión de los datos vectorizados
print("\nDimensiones de X (datos vectorizados):", X.shape)

# Dividir los datos en entrenamiento y prueba (80% entrenamiento, 20% prueba)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Mostrar el tamaño de los conjuntos de datos
print(f"\nTamaño del conjunto de entrenamiento: {X_train.shape}")
print(f"Tamaño del conjunto de prueba: {X_test.shape}")
