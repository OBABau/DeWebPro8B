import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Conexión como superuser para crear la base de datos
try:
    conn = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='190157',
        port='5432'
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    
    # Verificar si la base de datos existe
    cursor.execute("SELECT 1 FROM pg_database WHERE datname='nfl_db'")
    exists = cursor.fetchone()
    
    if not exists:
        cursor.execute('CREATE DATABASE nfl_db')
        print("Base de datos 'nfl_db' creada exitosamente.")
    else:
        print("Base de datos 'nfl_db' ya existe.")
    
    cursor.close()
    conn.close()
    print("Conexión a PostgreSQL exitosa.")
    
except Exception as e:
    print(f"Error al conectar a PostgreSQL: {e}")
