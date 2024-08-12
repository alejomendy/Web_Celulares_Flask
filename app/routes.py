from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Equipo

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/equipos')
def equipos():
    equipos = Equipo.query.all()
    return render_template('equipos.html', equipos=equipos)

@main_bp.route('/add_equipo', methods=['GET', 'POST'])
def add_equipo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        modelo = request.form['modelo']
        categoria = request.form['categoria']
        costo = float(request.form['costo'])
        nuevo_equipo = Equipo(nombre=nombre, modelo=modelo, categoria=categoria, costo=costo)
        db.session.add(nuevo_equipo)
        db.session.commit()
        return redirect(url_for('main.equipos'))
    return render_template('add_equipos.html')

@main_bp.route('/edit_equipo/<int:id>', methods=['GET', 'POST'])
def edit_equipo(id):
    equipo = Equipo.query.get_or_404(id)
    if request.method == 'POST':
        equipo.nombre = request.form['nombre']
        equipo.modelo = request.form['modelo']
        equipo.categoria = request.form['categoria']
        equipo.costo = float(request.form['costo'])
        db.session.commit()
        return redirect(url_for('main.equipos'))
    return render_template('edit_equipos.html', equipo=equipo)
