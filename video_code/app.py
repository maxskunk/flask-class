from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name':'My Wonderful Store',
        'items': [
            {
               'name':'My Item',
               'price' : 15.99 
            }
        ]
    }
]

@app.route('/') #http://google.com/

#Post = used to receive data
#Get = Send Daeta back

#Post /store data
@app.route('/store',methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)

#Get /store/string:name
@app.route('/store/<string:name>',methods=['GET'])
def get_store(name):
    #iterate over stores
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'store not found'})


#Get /store
@app.route('/store',methods=['GET'])
def get_stores():
    return jsonify({'stores': stores})

#Post /store/string:name/item
@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name' : request_data['name'],
                'price': request_data['price']
            }
            store['item'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})

    
#Get /store/<string:name>/item
@app.route('/store/<string:name>/item',methods=['GET'])
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
             return jsonify({'items':store['item']})
    return jsonify({'message':'store not found'})

app.run(port=5000)

