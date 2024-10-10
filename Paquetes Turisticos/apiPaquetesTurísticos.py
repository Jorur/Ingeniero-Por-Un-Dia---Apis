from flask import Flask, request, jsonify

app = Flask(__name__)

paquetes = [
    {
        'id': 1,
        'nombre': 'Playa Tropical',
        'descripcion': 'Disfruta de la playa y el sol',
        'urlImagen': 'https://media.gq.com.mx/photos/620e915c43f71a078a35533f/master/pass/playa.jpg',
        'precio': 1000
    },
    {
        'id': 2,
        'nombre': 'Aventura en las montañas',
        'descripcion': 'Disfruta de la naturaleza y la aventura de las majestuosas montañas',
        'urlImagen': 'https://as01.epimg.net/buenavida/imagenes/2017/04/19/portada/1492611810_905974_1492611976_noticia_normal.jpg',
        'precio': 800
    },
    {
        'id': 3,
        'nombre': 'Ciudad cosmopolita',
        'descripcion': 'Disfruta de la ciudad y la vida nocturna',
        'urlImagen': 'https://png.pngtree.com/thumb_back/fh260/background/20220812/pngtree-skyline-of-brisbane-queensland-australia-queensland-cosmopolitan-city-concrete-photo-image_25167244.jpg',
        'precio': 1200
    },
    {
        'id': 4,
        'nombre': 'Tour de vinos',
        'descripcion': 'Disfruta de la cultura del vino',
        'urlImagen': 'https://vinasantacruz.cl/wp-content/uploads/2019/06/03-FOTO-GRAN-CHAMAN.png',
        'precio': 1500
    },
    {
        'id': 5,
        'nombre': 'Tour de café',
        'descripcion': 'Disfruta de la cultura del café',
        'urlImagen': 'https://fincarosablanca-moon-prod.sfo3.digitaloceanspaces.com/sites/activities/organic-coffee-tour-and-cupping/fincarosablanca-coffee-tour-492x492-couple-examining-coffee-beans-01.jpg',
        'precio': 1300
    },
    {
        'id': 6,
        'nombre': 'Explorar la selva',
        'descripcion': 'Disfruta de la naturaleza y la aventura de la selva',
        'urlImagen': 'https://img.freepik.com/fotos-premium/explorador-estudiando-planta-selva-tropical_1169360-483.jpg',
        'precio': 1400
    }
]

@app.route('/paquetes')
def get_paquetes():
    return jsonify(paquetes)

@app.route('/paquetes/<int:paquete_id>')
def get_paquete(paquete_id):
    paquete = [paquete for paquete in paquetes if paquete['id'] == paquete_id]
    if len(paquete) == 0:
        return jsonify({'mensaje': 'Paquete no encontrado'})
    return jsonify(paquete[0])

@app.route('/paquetes', methods=['POST'])
def create_paquete():
    paquete = {
        'id': paquetes[-1]['id'] + 1,
        'nombre': request.json['nombre'],
        'descripcion': request.json['descripcion'],
        'urlImagen': request.json['urlImagen'],
        'precio': request.json['precio']
    }
    paquetes.append(paquete)
    return jsonify({'mensaje': 'Paquete creado exitosamente'})

@app.route('/paquetes/<int:paquete_id>', methods=['PUT'])
def update_paquete(paquete_id):
    paquete = [paquete for paquete in paquetes if paquete['id'] == paquete_id]
    if len(paquete) == 0:
        return jsonify({'mensaje': 'Paquete no encontrado'})
    paquete[0]['nombre'] = request.json.get('nombre', paquete[0]['nombre'])
    paquete[0]['descripcion'] = request.json.get('descripcion', paquete[0]['descripcion'])
    paquete[0]['urlImagen'] = request.json.get('urlImagen', paquete[0]['urlImagen'])
    paquete[0]['precio'] = request.json.get('precio', paquete[0]['precio'])
    return jsonify({'mensaje': 'Paquete actualizado exitosamente'})

@app.route('/paquetes/<int:paquete_id>', methods=['DELETE'])
def delete_paquete(paquete_id):
    paquete = [paquete for paquete in paquetes if paquete['id'] == paquete_id]
    if len(paquete) == 0:
        return jsonify({'mensaje': 'Paquete no encontrado'})
    paquetes.remove(paquete[0])
    return jsonify({'mensaje': 'Paquete eliminado exitosamente'})


if __name__ == '__main__':
    app.run(debug=True)