import os
import secrets
from flask_sqlalchemy import SQLAlchemy
import urllib.parse
import hashlib




params = urllib.parse.quote_plus(f"DRIVER={os.environ['DRIVER']};SERVER={os.environ['SERVER']};DATABASE={os.environ['DATABASE']};Trusted_Connection=yes;")

class Config:
    SECRET_KEY = secrets.token_hex()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % params

db = SQLAlchemy()