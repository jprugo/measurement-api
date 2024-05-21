from masoniteorm.connections import ConnectionResolver
from masoniteorm.config import db_url

DATABASES = {
  "default": "sqlite",
  "sqlite": db_url("sqlite:///measurements.db")
}

DB = ConnectionResolver().set_connection_details(DATABASES)