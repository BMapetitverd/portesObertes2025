from flask import Flask, render_template, request
from database.db_connection import get_db_connection
from database.models import create_tables
import config

app = Flask(__name__)
app.config.from_object(config)

# Crear tablas al iniciar
create_tables()

@app.route('/', methods=['GET', 'POST'])
def formulario_fp():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        fp_seleccionado = request.form['fp']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO solicitudes (nombre, apellido, fp) VALUES (%s, %s, %s)",
                (nombre, apellido, fp_seleccionado)
            )
            conn.commit()
            return render_template('success.html')
        except Exception as e:
            return f"<h1>Error</h1><p>{str(e)}</p>", 500
        finally:
            cursor.close()
            conn.close()
    
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)