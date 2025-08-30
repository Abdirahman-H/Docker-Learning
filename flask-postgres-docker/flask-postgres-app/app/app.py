from flask import Flask, render_template
import os
import psycopg2
import time

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "db")
DB_PORT = os.environ.get("DB_PORT", 5432)
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "mysecret")
DB_NAME = os.environ.get("DB_NAME", "mydb")

def get_db_connection():
    max_retries = 5
    for i in range(max_retries):
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                port=DB_PORT,
                user=DB_USER,
                password=DB_PASSWORD,
                dbname=DB_NAME
            )
            return conn
        except psycopg2.OperationalError as e:
            if i < max_retries - 1:
                print(f"Database connection failed. Retrying in 5 seconds... ({i+1}/{max_retries})")
                time.sleep(5)
            else:
                raise e

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT 'Hello from PostgreSQL!'")
    message = cur.fetchone()[0]
    cur.close()
    conn.close()
    return render_template("index.html", message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)