buyers_data = [
    {"name": "Juan Pérez", "age": 35, "income": 50000.00, "credit_score": 750, "occupation": "Ingeniero"},
    {"name": "María López", "age": 29, "income": 60000.00, "credit_score": 780, "occupation": "Doctora"},
    {"name": "Carlos García", "age": 40, "income": 45000.00, "credit_score": 720, "occupation": "Profesor"},
    {"name": "Ana Martínez", "age": 27, "income": 55000.00, "credit_score": 760, "occupation": "Diseñadora"},
    {"name": "Luis Hernández", "age": 33, "income": 48000.00, "credit_score": 740, "occupation": "Abogado"},
    {"name": "Sofía Gutiérrez", "age": 31, "income": 62000.00, "credit_score": 800, "occupation": "Analista"},
    {"name": "Miguel Fernández", "age": 45, "income": 58000.00, "credit_score": 700, "occupation": "Arquitecto"},
    {"name": "Laura Ramírez", "age": 36, "income": 67000.00, "credit_score": 810, "occupation": "Gerente"},
    {"name": "Fernando Torres", "age": 38, "income": 52000.00, "credit_score": 730, "occupation": "Contador"},
    {"name": "Andrea Ortiz", "age": 25, "income": 54000.00, "credit_score": 770, "occupation": "Consultora"},
    {"name": "Pedro Morales", "age": 30, "income": 49000.00, "credit_score": 740, "occupation": "Desarrollador"},
    {"name": "Isabel Cruz", "age": 34, "income": 61000.00, "credit_score": 780, "occupation": "Científica"},
    {"name": "Ricardo Castillo", "age": 39, "income": 53000.00, "credit_score": 720, "occupation": "Chef"},
    {"name": "Paula Medina", "age": 28, "income": 57000.00, "credit_score": 750, "occupation": "Publicista"},
    {"name": "Hugo Mendoza", "age": 42, "income": 60000.00, "credit_score": 770, "occupation": "Administrador"},
    {"name": "Mariana Vargas", "age": 32, "income": 63000.00, "credit_score": 800, "occupation": "Marketing"},
    {"name": "Jorge Rivera", "age": 37, "income": 51000.00, "credit_score": 730, "occupation": "Ingeniero"},
    {"name": "Valeria Silva", "age": 26, "income": 56000.00, "credit_score": 760, "occupation": "Diseñadora"},
    {"name": "Daniela Rojas", "age": 29, "income": 58000.00, "credit_score": 750, "occupation": "Abogada"},
    {"name": "Cristian Vargas", "age": 41, "income": 54000.00, "credit_score": 720, "occupation": "Profesor"},
    {"name": "Patricia Aguirre", "age": 35, "income": 59000.00, "credit_score": 770, "occupation": "Doctora"},
    {"name": "Roberto Salazar", "age": 33, "income": 47000.00, "credit_score": 710, "occupation": "Arquitecto"},
    {"name": "Karina Esquivel", "age": 28, "income": 62000.00, "credit_score": 780, "occupation": "Gerente"},
    {"name": "Diego Gómez", "age": 44, "income": 55000.00, "credit_score": 730, "occupation": "Analista"},
    {"name": "Elena Paredes", "age": 31, "income": 61000.00, "credit_score": 770, "occupation": "Contadora"},
    {"name": "César Ortega", "age": 36, "income": 53000.00, "credit_score": 720, "occupation": "Desarrollador"},
    {"name": "Lucía Herrera", "age": 27, "income": 56000.00, "credit_score": 760, "occupation": "Consultora"},
    {"name": "Antonio Pérez", "age": 39, "income": 50000.00, "credit_score": 740, "occupation": "Chef"},
    {"name": "Gabriela Ramos", "age": 30, "income": 59000.00, "credit_score": 770, "occupation": "Abogada"},
    {"name": "Francisco Suárez", "age": 38, "income": 52000.00, "credit_score": 730, "occupation": "Científico"},
    {"name": "Diana Peña", "age": 29, "income": 60000.00, "credit_score": 780, "occupation": "Publicista"},
    {"name": "José Vázquez", "age": 45, "income": 48000.00, "credit_score": 710, "occupation": "Administrador"},
    {"name": "Marta Cárdenas", "age": 34, "income": 62000.00, "credit_score": 790, "occupation": "Marketing"},
    {"name": "Álvaro Campos", "age": 40, "income": 50000.00, "credit_score": 720, "occupation": "Ingeniero"},
    {"name": "Sandra León", "age": 28, "income": 57000.00, "credit_score": 750, "occupation": "Diseñadora"},
    {"name": "Héctor Gálvez", "age": 33, "income": 55000.00, "credit_score": 730, "occupation": "Abogado"},
    {"name": "Verónica Lozano", "age": 31, "income": 61000.00, "credit_score": 770, "occupation": "Profesora"},
    {"name": "Tomás Chávez", "age": 37, "income": 53000.00, "credit_score": 740, "occupation": "Analista"},
    {"name": "Claudia Quintana", "age": 32, "income": 60000.00, "credit_score": 760, "occupation": "Consultora"},
    {"name": "Fabián Soto", "age": 41, "income": 52000.00, "credit_score": 730, "occupation": "Arquitecto"},
    {"name": "Paola Jiménez", "age": 26, "income": 57000.00, "credit_score": 770, "occupation": "Gerente"},
    {"name": "Mario Vega", "age": 30, "income": 54000.00, "credit_score": 750, "occupation": "Chef"},
    {"name": "Luz Torres", "age": 34, "income": 59000.00, "credit_score": 780, "occupation": "Científica"},
    {"name": "Javier Blanco", "age": 35, "income": 51000.00, "credit_score": 740, "occupation": "Administrador"},
    {"name": "Nora Rivas", "age": 28, "income": 61000.00, "credit_score": 790, "occupation": "Marketing"},
    {"name": "Sebastián Cruz", "age": 36, "income": 48000.00, "credit_score": 720, "occupation": "Ingeniero"},
    {"name": "Adriana Morales", "age": 29, "income": 58000.00, "credit_score": 760, "occupation": "Diseñadora"},
    {"name": "Esteban Ruiz", "age": 44, "income": 52000.00, "credit_score": 740, "occupation": "Abogado"}
]
