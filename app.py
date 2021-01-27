from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {'name': 'Item 1', 'price': 15.98}
        ]
    }
]


@app.route('/')
def index():
    return "Hello, World"


@app.route('/health')
def sanity_Check():
    return "OK"


@app.route('/store')
def get_stores():
    return jsonify({'data': stores})


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()

    new_store = {
        'name': request_data['name'],
        'items': []
    }

    stores.append(new_store)

    return jsonify({'data': new_store})


@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'data': store})

    return jsonify({'message': 'No Store Found'})


@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'data': store['items']})

    return jsonify({'message': 'No Store Found'})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            request_data = request.get_json()

            new_item = {
                'name': request_data['name'],
                'price': request_data['price'],
            }

            store['items'].append(new_item)

            return jsonify({'data': new_item})

    return jsonify({'message': 'No Store Found'})


app.run(port=5000)
