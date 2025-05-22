from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    try:
        conn = psycopg2.connect(
            host='db',
            database='testdb',
            user='postgres',
            password='postgres'
        )
        conn.close()
        return "¡Conexión a base de datos exitosa!"
    except Exception as e:
        return f"Error al conectar: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
