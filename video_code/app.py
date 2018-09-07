from flask import Flask, jsonify

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
    pass

#Get /store/string:name
@app.route('/store/<string:name>',methods=['GET'])
def get_store(name):
    pass

#Get /store
@app.route('/store',methods=['GET'])
def get_stores():
    return jsonify({'stores': stores})

#Post /store/string:name/item
@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
    pass

#Get /store/<string:name>/item
@app.route('/store/<string:name>/item',methods=['GET'])
def get_item_in_store(name):
    pass

app.run(port=5000)

