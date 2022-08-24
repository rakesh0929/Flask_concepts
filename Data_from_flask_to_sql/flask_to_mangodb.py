from flask import Flask,jsonify,request
import pymongo



''' CREATE A MONGO DB DATABASE AND CONNECT IT TO HOSTNAME CONNECTION'''

client = pymongo.MongoClient("mongodb://localhost:27017/")   ## if you installed mongodb then  this is your localhost for mongodb
db = client["Task_day"]   ## create a databse
collections = db["Task_1"]  ## this collection is like creating a table in mongodb

# collections.insert_many({name:"Rakesh",number:987})


''' FLASK CODE IS AVALIABLE HERE DOWN'''

app = Flask(__name__)

@app.route("/mongo/insert",methods=["POST","GET"])
def insert():
    if(request.method == "POST"):
        name = request.json["name"]
        number = request.json["number"]
        collections.insert_one({"name":name , "number":number})
        return jsonify(str("successfly inserted record "))


# db.collection.update(  { _id:...} , { $set: { some_key.param2 : new_info  } }
## update a record
    
@app.route("/mongo/update",methods=["POST","GET"])
def update():
    if(request.method == "POST"):
        get_name = request.json["get_name"]
        # number = request.json["number"]
        collections.update_many({"name": get_name},{"$set":{"number" : 50000}})
        return jsonify(str("successfly updated record "))

## delete a record

@app.route("/mongo/delete",methods=["POST","GET"])
def delete():
    if(request.method == "POST"):
        del_name = request.json["del_name"]
        # number = request.json["number"]
        collections.delete_one({"name": del_name})
        return jsonify(str("successfly deleted record "))


## fetch records


@app.route("/mongo/fetch",methods=["POST","GET"])
def fetch():
    if(request.method == "POST"):
        k = collections.find()
        l = []                          ## you can see in the postman
        for i in k:
            l.append(i)
        return jsonify(str(l))

if __name__ == "__main__":
    app.run(debug=True)

