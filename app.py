from flask import Flask, render_template, request, redirect, url_for
from almacenamiento import cargar_eventos, guardar_eventos, generar_codigo

app = Flask(__name__)

# Lista en memoria para almacenar los eventos
eventos = []

# Página de inicio
@app.route('/')
def inicio():
    return render_template('index.html')

# Registrar un nuevo evento
@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    # Cargamos los eventos actuales desde el archivo JSON---01
    eventos = cargar_eventos()

    if request.method == "POST":
        evento = {
            'codigo': request.form['codigo'].upper().strip(),
            'tipo': request.form['tipo'],
            'equipo': request.form['equipo'],
            'nivel': request.form['nivel'],
            'estado': request.form['estado']
        }
        eventos.append(evento)

        # Guardamos la lista actualizada en eventos.json ----------02
        guardar_eventos(eventos)


        return redirect(url_for('listar'))
    return render_template('registrar.html')

# Listar todos los eventos
@app.route('/listar')
def listar():
    eventos = cargar_eventos() #03
    return render_template('listar.html', eventos=eventos)

'''
# Consultar un evento por código
@app.route('/consulta', methods=['GET', 'POST'])
def consulta():
    evento = None
    if request.method == 'POST':
        codigo = request.form['codigo'].upper()
        evento = next((e for e in eventos if e['codigo'] == codigo), None)
    return render_template('consulta.html', evento=evento)
'''

@app.route('/consulta', methods=['GET', 'POST'])
def consulta():
    evento = None
    codigo = request.args.get('codigo') or (request.form.get('codigo') if request.method == 'POST' else None)
    
    if codigo:
        codigo_limpio = codigo.upper().strip()
        evento = next((e for e in eventos if e['codigo'] == codigo_limpio), None)
        
    return render_template('consulta.html', evento=evento)

if __name__ == '__main__':
    app.run(debug=True)