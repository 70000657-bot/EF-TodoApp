from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tareas = []
contador_id = 1

@app.route('/')
def index():
    return render_template('index.html', tareas=tareas)

@app.route('/agregar', methods=['POST'])
def agregar():
    global contador_id
    titulo = request.form.get('titulo', '').strip()
    if titulo:
        tareas.append({'id': contador_id, 'titulo': titulo, 'completada': False})
        contador_id += 1
    return redirect(url_for('index'))

@app.route('/completar/<int:tarea_id>')
def completar(tarea_id):
    for tarea in tareas:
        if tarea['id'] == tarea_id:
            tarea['completada'] = not tarea['completada']
    return redirect(url_for('index'))

@app.route('/eliminar/<int:tarea_id>')
def eliminar(tarea_id):
    global tareas
    tareas = [t for t in tareas if t['id'] != tarea_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
