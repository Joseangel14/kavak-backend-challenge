import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from joblib import dump
import logging
import sys
import os

# Agregar la raíz del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from seed_data_files.buyers_data import buyers_data
from seed_data_files.credit_applications_data import credit_applications_data
from seed_data_files.vehicles_data import vehicles_data

# Cargar y preparar datos
def load_data():
    buyers = pd.DataFrame(buyers_data)
    credit_applications = pd.DataFrame(credit_applications_data)
    vehicles = pd.DataFrame(vehicles_data)

    # Renombrar/agregar columnas
    vehicles["id_vehicle"] = range(1, len(vehicles) + 1)
    vehicles.rename(columns={"price": "vehicle_price"}, inplace=True)

    # Merge de las tablas
    data = credit_applications.merge(buyers, left_on="buyer_id", right_index=True)
    data = data.merge(vehicles, left_on="vehicle_id", right_on="id_vehicle")

    # Verificar valores únicos en 'status'
    logger.info(f"Valores únicos de 'status' antes del mapeo: {data['status'].unique()}")

    # Filtrar valores válidos ('Approved', 'Denied')
    valid_status = ["Approved", "Denied"]
    filtered_data = data[data["status"].isin(valid_status)]

    # Mapear 'status' a binario
    y = filtered_data["status"].map({"Approved": 1, "Denied": 0})

    # Asegurarse de que no hay valores NaN
    if y.isna().any():
        logger.error("Valores NaN encontrados en 'y'. Revisa los valores en 'status'.")
        raise ValueError("Valores no mapeados en 'status'. Verifica el conjunto de datos.")

    # Selección de variables
    X = filtered_data[["income", "credit_score", "age", "vehicle_price", "occupation"]]
    logger.info(f"Estructura de X después de selección: {X.columns}")

    return X, y


# Entrenar el modelo
def train_model(X, y):
    # Dividir los datos
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Preprocesamiento
    numeric_features = ["income", "credit_score", "age", "vehicle_price"]
    categorical_features = ["occupation"]

    numeric_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(handle_unknown="ignore")

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features),
        ]
    )

    # Modelo
    model = RandomForestClassifier(random_state=42)
    pipeline = Pipeline(steps=[("preprocessor", preprocessor), ("classifier", model)])

    # Entrenar modelo
    logger.info("Entrenando el modelo...")
    pipeline.fit(X_train, y_train)

    # Evaluar modelo
    accuracy = pipeline.score(X_test, y_test)
    logger.info(f"Exactitud del modelo: {accuracy * 100:.2f}%")

    # Guardar modelo
    dump(pipeline, "machine_learning/credit_model.joblib")
    logger.info("Modelo guardado en 'machine_learning/credit_model.joblib'.")

if __name__ == "__main__":
    X, y = load_data()
    train_model(X, y)
