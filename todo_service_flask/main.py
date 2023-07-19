from flask import Flask, request, Response

import helper
import json
app = Flask(__name__)
port = 5100


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/item/new', methods=['POST'])
def add_item():
    # Get item from the POST body
    req_data = request.get_json()
    item = req_data['item']

    # Add item to the list
    res_data = helper.add_to_list(item)

    # Return error if item not added
    if res_data is None:
        response = Response("{'error': 'Item not added - " + item + "'}", status=400, mimetype='application/json')
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response

#покажи все
@app.route('/items/all')
def get_all_items():
    res_data = helper.get_all_items()
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response


@app.route('/item/remove', methods=['DELETE'])
def delete_item():
    # Get item from the POST body
    req_data = request.get_json()
    item = req_data['item']

    # Delete item from the list
    res_data = helper.delete_item(item)

    # Return error if the item could not be deleted
    if res_data is None:
        response = Response("{'error': 'Error deleting item - '" + item + "}", status=400, mimetype='application/json')
    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)