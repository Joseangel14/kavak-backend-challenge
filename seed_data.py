from app.db import SessionLocal
from app.models.vehicle import Vehicle
from app.models.feedback import Feedback
from app.models.buyer import Buyer
from app.models.credit_application import CreditApplication
from datetime import datetime
import logging

# Importar datos desde los archivos
from seed_data_files.vehicles_data import vehicles_data
from seed_data_files.feedback_data import feedback_data
from seed_data_files.buyers_data import buyers_data
from seed_data_files.credit_applications_data import credit_applications_data

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Función genérica para insertar datos en la base de datos
def bulk_insert(db, model, data, table_name):
    if db.query(model).count() == 0:
        logger.info(f"Tabla '{table_name}' vacía. Insertando datos iniciales...")
        objects = [model(**item) for item in data]
        db.bulk_save_objects(objects)
        logger.info(f"Datos iniciales de '{table_name}' insertados correctamente.")
    else:
        logger.info(f"La tabla '{table_name}' ya contiene datos. No se insertaron duplicados.")

# Función para insertar datos iniciales de vehículos y feedback
def seed_vehicles_and_feedback():
    db = SessionLocal()
    try:
        with db.begin():
            # Insertar vehículos
            bulk_insert(db, Vehicle, vehicles_data, "vehicles")

            # Insertar feedback
            feedback_entries = []
            for feedback in feedback_data:
                feedback["date"] = datetime.strptime(feedback["date"], "%Y-%m-%d").date()
                vehicle = db.query(Vehicle).filter(Vehicle.id == feedback["vehicle_id"]).first()
                if vehicle:
                    feedback_entries.append({
                        "vehicle_id": feedback["vehicle_id"],
                        "rating": feedback["rating"],
                        "comment": feedback["comment"],
                        "date": feedback["date"],
                    })
                else:
                    logger.warning(f"Vehículo con ID {feedback['vehicle_id']} no encontrado. Saltando entrada de feedback.")
            feedback_objects = [Feedback(**entry) for entry in feedback_entries]
            db.bulk_save_objects(feedback_objects)
            logger.info("Datos iniciales de feedback insertados correctamente.")
    except Exception as e:
        logger.error(f"Error al insertar datos iniciales de vehículos y feedback: {e}", exc_info=True)
    finally:
        db.close()

# Función para insertar datos iniciales de compradores y solicitudes de crédito
def seed_buyers_and_credit_applications():
    db = SessionLocal()
    try:
        with db.begin():
            # Insertar compradores
            bulk_insert(db, Buyer, buyers_data, "buyers")

            # Insertar solicitudes de crédito
            credit_applications = []
            for application in credit_applications_data:
                buyer = db.query(Buyer).filter(Buyer.id == application["buyer_id"]).first()
                vehicle = db.query(Vehicle).filter(Vehicle.id == application["vehicle_id"]).first()
                if buyer and vehicle:
                    credit_applications.append({
                        "buyer_id": application["buyer_id"],
                        "vehicle_id": application["vehicle_id"],
                        "approved_limit": application.get("approved_limit", 0.0),
                        "status": application.get("status", "Pending"),
                    })
                else:
                    logger.warning(
                        f"Datos faltantes para buyer_id {application['buyer_id']} o vehicle_id {application['vehicle_id']}. Saltando."
                    )
            credit_application_objects = [CreditApplication(**entry) for entry in credit_applications]
            db.bulk_save_objects(credit_application_objects)
            logger.info("Datos iniciales de solicitudes de crédito insertados correctamente.")
    except Exception as e:
        logger.error(f"Error al insertar datos iniciales de compradores y solicitudes de crédito: {e}", exc_info=True)
    finally:
        db.close()

# Ejecutar el script directamente si se llama este archivo
if __name__ == "__main__":
    seed_vehicles_and_feedback()
    seed_buyers_and_credit_applications()
