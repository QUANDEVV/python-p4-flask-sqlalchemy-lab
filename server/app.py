#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.get(id)
    zookeeper = Zookeeper.query.get(id)
    enclosure = Enclosure.query.get(id)
    return f'<ul>ID: {animal.id}</ul><ul>Name: {animal.name}</ul><ul>Species: {animal.species}</ul><ul>Zookeeper: {zookeeper.name}</ul><ul>Enclosure: {enclosure.environment}</ul></ul>'


@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.get(id)
    if zookeeper:
        return f'<ul>ID: {zookeeper.id}</ul><ul>Name: {zookeeper.name}</ul><ul>Birthday: {zookeeper.birthday}</ul>'
    else:
        return f'Zookeeper with ID {id} not found.'

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.get(id)
    if enclosure:
        return f'<ul>ID: {enclosure.id}</ul><ul>Enclosure: {enclosure.environment}</ul>Open to visitots: {enclosure.open_to_visitors}</ul>'
    else:
        return f'Enclosure with ID {id} not found.'



if __name__ == '__main__':
    app.run(port=5555, debug=True)