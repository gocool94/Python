from flask import Flask , request

app = Flask(__name__)


stores = [
    {
        "name":"MyStore",
        "items":[
                    {
                        "name":"Chair",
                        "Price":24
                    },
                     {
                         "name":"book",
                         "price":26
                     }
        ]
    }
]


@app.get("/store")
def get_stores():
    return {"stores":stores}

@app.post("/store")
def post_stores():
    request_data = request.get_json()
    new_store = {"name":request_data["name"],"items":[]}
    stores.append(new_store)
    return stores, 201

@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    print(request_data)
    #return name
    #return request_data
    for store in stores:
        if store["name"] == name:
            new_item = {"name":request_data["name"], "price":request_data["price"]}
            store["items"].append(new_item)
            #return request_data
            return new_item, 201
    return {"message": "Store not found"}, 404

@app.get("/store/<string:name>/")
def get_specific_store(name):
    for store in stores:
        print(store)
        if store["name"] == name:
            return store
    return {"Message":"Link not found"}, 404 
    

    

    


if __name__ == '__main__':
    app.debug = True
    app.run()
    



