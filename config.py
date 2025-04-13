import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Configuración de MySQL
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.getenv('MYSQL_USER', 'admin')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'Curs202425')
    MYSQL_DB = os.getenv('MYSQL_DB', 'borjaMoll')