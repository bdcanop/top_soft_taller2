import json
from flask import Flask, jsonify, render_template, send_from_directory
import random

app = Flask(__name__)

pokemons = [
        {
            'id': 1,
            'nombre': 'Mario',
            'imagen': '/pokeneas_sin_refinar/ay_mario.jpeg',  
            'frase': "¡Ay Mario Gonorrea!",
            'altura': 1.6,
            'habilidad': 'Fuego control'
        },
        {
            'id': 2,
            'nombre': 'Checho',
            'imagen': '/pokeneas_sin_refinar/checho.jpg',  
            'frase': "¡Ey Checho un saludo pa las perras!",
            'altura': 1.7,
            'habilidad': 'Saludar a las perras'
        },
        {
            'id': 3,
            'nombre': 'Del verde',
            'imagen': '/pokeneas_sin_refinar/del_verde.jpg',  
            'frase': "¡Mis abuelos me hicieron del verde, que viva la marihuana hp!",
            'altura': 1.72,
            'habilidad': 'Fumar bareta'
        },
        {
            'id': 4,
            'nombre': 'Fuisioso',
            'imagen': '/pokeneas_sin_refinar/fuisioso.jpg',  
            'frase': "¿Sabe qué?, sólo nacional a morir, ¿sabe qué?, ¡sólo nacional!, ¡FUISIOSOS!",
            'altura': 1.67,
            'habilidad': 'Apoyar al nacinal'
        },
        {
            'id': 5,
            'nombre': '¡Los niños!',
            'imagen': '/pokeneas_sin_refinar/fumanchar.jpg',  
            'frase': "¿Qué vamos a hacer pues hoy? ¿Qué hay pa la cabeza? pa las fumancharias, sólo San Javier, ¿a dónde hay que llegar?",
            'altura': 1.68,
            'habilidad': 'Correr con más de cinco celulares en cada mano'
        },
        {
            'id': 6,
            'nombre': 'No sé pai',
            'imagen': '/pokeneas_sin_refinar/no_se_pai.jpg',  
            'frase': "¿La capital de Bangladesh?, no se pai, estoy gruchis porque tuqui tuqui muñeco alal, como yo no salgo de aquí, Medellín, Itaguí...",
            'altura': 1.64,
            'habilidad': 'Viajar'
        },
        {
            'id': 7,
            'nombre': 'Zarco',
            'imagen': '/pokeneas_sin_refinar/zarco.jpg',  
            'frase': "¿Usted por qué se deja llenar la cabeza mamá?, ¿Por qué?, ¿Por qué se deja confundir?, ¿Usted no cree en mí?",
            'altura': 1.75,
            'habilidad': 'Labia'
        }
    ]

@app.route('/pokemon_info')
def get_random_pokemon_info():
    random_pokemon = random.choice(pokemons)
    return jsonify(json.dumps({
        'id': random_pokemon['id'],
        'nombre': random_pokemon['nombre'],
        'altura': random_pokemon['altura'],
        'habilidad': random_pokemon['habilidad'],
    }, sort_keys=False))

@app.route('/random_pokemon')
def show_random_pokemon():
    
    random_pokemon = random.choice(pokemons)
    return render_template('pokemon.html', id_del_contenedor=1, pokemon=random_pokemon)

# Ruta para servir imágenes estáticas
@app.route('/static/<filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(port=8080)  # Escuchar en todas las interfaces en el puerto 5000
