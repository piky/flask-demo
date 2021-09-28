import os

# Database authentication settings
class DevelopmentConfig(Config):
    DB_SERVER = 'mysqldb'
    DB_URI = 'inventory'
    DB_USER = 'root'
    DB_PASSWORD = os.environ.get("MYSQL_ROOT_PASSWORD")
