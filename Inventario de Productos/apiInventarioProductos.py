from flask import Flask, request, jsonify

app = Flask(__name__)

productos = [
    {
        'id': 1,
        'categoria': 'Laptop',
        'marca': 'HP',
        'modelo': 'Pavilion 15',
        'urlImagen': 'https://m.media-amazon.com/images/I/61e4ni3WBrL._AC_SL1000_.jpg',
        'precio': 1000
    },
    {
        'id': 2,
        'categoria': 'Laptop',
        'marca': 'Dell',
        'modelo': 'Inspiron 15',
        'urlImagen': 'https://m.media-amazon.com/images/I/71jrNWixkbS._AC_SL1500_.jpg',
        'precio': 800
    },
    {
        'id': 3,
        'categoria': 'Laptop',
        'marca': 'Lenovo',
        'modelo': 'IdeaPad 3',
        'urlImagen': 'https://i0.wp.com/bitstorebolivia.com/wp-content/uploads/2023/04/Lenovo-IdeaPad-3-14ITL05-6-1.jpg?fit=1080%2C1080&ssl=1',
        'precio': 1200
    },
    {
        'id': 4,
        'categoria': 'Laptop',
        'marca': 'Asus',
        'modelo': 'VivoBook 15',
        'urlImagen': 'https://m.media-amazon.com/images/I/71kMPSNqHbL._AC_SL1500_.jpg',
        'precio': 1500
    },
    {
        'id': 5,
        'categoria': 'Laptop',
        'marca': 'Acer',
        'modelo': 'Aspire 5',
        'urlImagen': 'https://sysbol.com/2018-large_default/acer-aspire-5-slim-a515-46-r14k-156-amd-ryzen-3-3350u-4gb-ssd-nvme-de-128-gb-win-10-home-modo-s.jpg',
        'precio': 1300,
    },
    {
        'id': 6,
        'categoria': 'Laptop',
        'marca': 'Apple',
        'modelo': 'MacBook Air',
        'urlImagen': 'https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/macbookair-og-202402?wid=1200&hei=630&fmt=jpeg&qlt=95&.v=1707414684423',
        'precio': 1400
    }
]

@app.route('/productos')
def get_productos():
    return jsonify(productos)

@app.route('/productos/<int:producto_id>')
def get_producto(producto_id):
    producto = [producto for producto in productos if producto['id'] == producto_id]
    if len(producto) == 0:
        return jsonify({'mensaje': 'Producto no encontrado'})
    return jsonify(producto[0])

@app.route('/productos', methods=['POST'])
def create_producto():
    producto = {
        'id': productos[-1]['id'] + 1,
        'categoria': request.json['categoria'],
        'marca': request.json['marca'],
        'modelo': request.json['modelo'],
        'urlImagen': request.json['urlImagen'],
        'precio': request.json['precio']
    }
    productos.append(producto)
    return jsonify({'mensaje': 'Producto creado exitosamente'})

@app.route('/productos/<int:producto_id>', methods=['PUT'])
def update_producto(producto_id):
    producto = [producto for producto in productos if producto['id'] == producto_id]
    if len(producto) == 0:
        return jsonify({'mensaje': 'Producto no encontrado'})
    producto[0]['categoria'] = request.json.get('categoria', producto[0]['categoria'])
    producto[0]['marca'] = request.json.get('marca', producto[0]['marca'])
    producto[0]['modelo'] = request.json.get('modelo', producto[0]['modelo'])
    producto[0]['urlImagen'] = request.json.get('urlImagen', producto[0]['urlImagen'])
    producto[0]['precio'] = request.json.get('precio', producto[0]['precio'])
    return jsonify({'mensaje': 'Producto actualizado exitosamente'})

@app.route('/productos/<int:producto_id>', methods=['DELETE'])
def delete_producto(producto_id):
    producto = [producto for producto in productos if producto['id'] == producto_id]
    if len(producto) == 0:
        return jsonify({'mensaje': 'Producto no encontrado'})
    productos.remove(producto[0])
    return jsonify({'mensaje': 'Producto eliminado exitosamente'})

if __name__ == '__main__':
    app.run(debug=True)