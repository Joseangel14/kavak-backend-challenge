import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app.main import app
from app.db import engine, Base
from app.schemas.vehicle import VehicleResponse  # Importa el esquema de respuesta

# Crear cliente de pruebas
client = TestClient(app)

# Fixture para limpiar y preparar la base de datos antes de cada test
@pytest.fixture(scope="function", autouse=True)
def clean_db():
    """
    Limpia la base de datos antes de cada prueba eliminando y recreando las tablas.
    """
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

# Mockear la sesión de base de datos
@patch("app.db.SessionLocal")
def test_create_and_get_vehicle(mocked_session):
    # Simular los datos de la base de datos
    mocked_db_instance = MagicMock()
    mocked_session.return_value = mocked_db_instance

    # Crear un objeto Mock que cumpla con el esquema de respuesta
    mocked_vehicle = VehicleResponse(
        id=1,
        brand="Toyota",
        model="Corolla",
        year=2022,
        price=20000.00,
    )
    mocked_vehicle_dict = mocked_vehicle.model_dump()

    # Simular el comportamiento del mock para la consulta
    mocked_db_instance.query.return_value.filter.return_value.first.return_value = mocked_vehicle_dict
    mocked_db_instance.query.return_value.offset.return_value.limit.return_value.all.return_value = [mocked_vehicle_dict]

    # Simular la creación de un vehículo (asignar id manualmente)
    def mock_add(vehicle):
        vehicle.id = 1  # Simular asignación de ID
        return None

    mocked_db_instance.add.side_effect = mock_add

    # Obtener token
    response = client.post("/token", data={"username": "testuser", "password": "password123"})
    assert response.status_code == 200, f"Error al obtener token: {response.json()}"
    token = response.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}

    # Crear vehículo
    create_response = client.post(
        "/vehicles/",
        json={"brand": "Toyota", "model": "Corolla", "year": 2022, "price": 20000.00},
        headers=headers,
    )
    assert create_response.status_code == 200, f"Error al crear vehículo: {create_response.json()}"
    created_vehicle = create_response.json()
    assert created_vehicle["id"] == 1  # Verifica que el ID sea 1
    assert created_vehicle["brand"] == "Toyota"

    # Obtener vehículos
    get_response = client.get("/vehicles/", headers=headers)
    assert get_response.status_code == 200
    vehicles = get_response.json()
    assert len(vehicles) > 0
    assert any(vehicle["id"] == 1 for vehicle in vehicles)