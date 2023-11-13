# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return '¡Hola, Pokedex!'

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, jsonify, render_template, send_from_directory
import random

app = Flask(__name__)

# Ruta para obtener información de un Pokemon aleatorio
@app.route('/pokemon_info')
def get_random_pokemon_info():
    pokemons = [
        {
            'id': 1,
            'nombre': 'Bulbasaur',
            'altura': 0.4,
            'habilidad': 'Agua',
        },
        # Agrega más Pokemon aquí
    ]
    random_pokemon = random.choice(pokemons)
    return jsonify({'id_del_contenedor': 1, **random_pokemon})

# Ruta para mostrar imagen y frase de un Pokemon aleatorio
@app.route('/random_pokemon')
def show_random_pokemon():
    pokemons = [
        {
            'id': 1,
            'nombre': 'Bulbasaur',
            'imagen': '/random_pokemon/bulbasaur.png',  # Agrega la ruta de la imagen
            'frase': '¡Ey qhubo pues!',
        },
        {
            'id': 2,
            'nombre': 'Caterpie',
            'imagen': '/random_pokemon/caterpie.png',  # Agrega la ruta de la imagen
            'frase': '¡Ey qhubo pues!',
        },
        {
            'id': 3,
            'nombre': 'Charmander',
            'imagen': '/random_pokemon/charmander.png',  # Agrega la ruta de la imagen
            'frase': '¡Ey qhubo pues!',
        },
        {
            'id': 4,
            'nombre': 'Pidgey',
            'imagen': '/random_pokemon/pidgey.png',  # Agrega la ruta de la imagen
            'frase': '¡Ey qhubo pues!',
        },
        {
            'id': 5,
            'nombre': 'Rattata',
            'imagen': '/random_pokemon/rattata.png',  # Agrega la ruta de la imagen
            'frase': '¡Ey qhubo pues!',
        },
        {
            'id': 6,
            'nombre': 'Squirtle',
            'imagen': '/random_pokemon/squirtle.png',  # Agrega la ruta de la imagen
            'frase': '¡Ey qhubo pues!',
        },
        {
            'id': 7,
            'nombre': 'Weedle',
            'imagen': '/random_pokemon/weedle.png',  # Agrega la ruta de la imagen
            'frase': '¡Ey qhubo pues!',
        }
        # Agrega más Pokemon aquí
    ]
    random_pokemon = random.choice(pokemons)
    return render_template('pokemon.html', id_del_contenedor=1, pokemon=random_pokemon)

# Ruta para servir imágenes estáticas
@app.route('/static/<filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)