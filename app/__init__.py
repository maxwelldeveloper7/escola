from flask import Flask
import psycopg

app = Flask(__name__)

def conectar_db():
    return psycopg.connect("host=192.168.0.182 dbname=escola_db user=postgres password=postgres")

from app import routes