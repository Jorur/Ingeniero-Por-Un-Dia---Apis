from flask import Flask, request, jsonify

app = Flask(__name__)

memes = [
    {
        'id': 1,
        'nombre': 'Programadores vs. Diseñadores',
        'descripcion': 'Un meme de la diferencia entre un programador y un diseñador',
        'urlImagen': 'https://www.boredpanda.es/blog/wp-content/uploads/2022/03/03-6228a2ac81c49_hwurhp7crzf81-png__700-622b13a1722c6__700.jpg'
    },
    {
        'id': 2,
        'nombre': 'Entender codigo anterior',
        'descripcion': 'Cuando te toca entender el codigo de alguien mas',
        'urlImagen': 'https://media.makeameme.org/created/yo-intentando-entender-12decb5828.jpg'
    },
    {
        'id': 3,
        'nombre': 'Aplicacion imposible',
        'descripcion': 'Cuando te piden una aplicacion imposible',
        'urlImagen': 'https://www.boredpanda.es/blog/wp-content/uploads/2022/03/15-6228a4f967d71_0rue2pamjx781__700-622b1e159fe28__700.jpg'
    },
    {
        'id': 4,
        'nombre': 'Programador de videojuegos',
        'descripcion': 'Lo que todos queriamos ser',
        'urlImagen': 'https://cdn.memegenerator.es/imagenes/memes/full/23/32/23320723.jpg'
    },
    {
        'id': 5,
        'nombre': 'Programador en la vida real',
        'descripcion': 'La realidad de ser programador',
        'urlImagen': 'https://i.pinimg.com/236x/5f/0b/37/5f0b373ca180866929c9bc860f2f72a0.jpg'
    }
]

@app.route('/meme')
def get_memes():
    return jsonify(memes)

@app.route('/meme/<int:meme_id>')
def get_meme(meme_id):
    meme = [meme for meme in memes if meme['id'] == meme_id]
    if len(meme) == 0:
        return jsonify({'mensaje': 'Meme no encontrado'})
    return jsonify(meme[0])

@app.route('/meme', methods=['POST'])
def create_meme():
    meme = {
        'id': memes[-1]['id'] + 1,
        'nombre': request.json['nombre'],
        'descripcion': request.json['descripcion'],
        'urlImagen': request.json['urlImagen']
    }
    memes.append(meme)
    return jsonify({'mensaje': 'Meme creado exitosamente'})

@app.route('/meme/<int:meme_id>', methods=['PUT'])
def update_meme(meme_id):
    meme = [meme for meme in memes if meme['id'] == meme_id]
    if len(meme) == 0:
        return jsonify({'mensaje': 'Meme no encontrado'})
    meme[0]['nombre'] = request.json.get('nombre', meme[0]['nombre'])
    meme[0]['descripcion'] = request.json.get('descripcion', meme[0]['descripcion'])
    meme[0]['urlImagen'] = request.json.get('urlImagen', meme[0]['urlImagen'])
    return jsonify({'mensaje': 'Meme actualizado exitosamente'})

@app.route('/meme/<int:meme_id>', methods=['DELETE'])
def delete_meme(meme_id):
    meme = [meme for meme in memes if meme['id'] == meme_id]
    if len(meme) == 0:
        return jsonify({'mensaje': 'Meme no encontrado'})
    memes.remove(meme[0])
    return jsonify({'mensaje': 'Meme eliminado exitosamente'})

if __name__ == '__main__':
    app.run(debug=True)