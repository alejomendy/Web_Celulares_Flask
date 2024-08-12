from app import db

class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    modelo = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    costo = db.Column(db.Float, nullable=False)
