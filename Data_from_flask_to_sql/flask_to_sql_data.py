from flask import Flask ,jsonify,request,render_template
import mysql.connector as connection

''' CREATE A DATABSE USING THE CONNECT AND CURSOR AND EXECUTE SO THAT THE DATA BASE IS CONNECTED'''

mydb = connection.connect(host="localhost",user="root", passwd="Rakesh@12345678",use_pure=True,port=3307)   ## connecting to sql
cursor = mydb.cursor()           ## making cursor to execute
cursor.execute("CREATE DATABASE IF NOT EXISTS flask_task_db")    # create a DB if not exists
cursor.execute("CREATE TABLE IF NOT EXISTS flask_task_db.task_1(name varchar(30),number int)")  ## create a table if not exists

''' FLASK CODE STATS HERE AFTER THE DATABASE IS SETUP'''

app = Flask(__name__)

## insert a record into databse

@app.route("/insert",methods=["POST","GET"])
def insert():  ## to insert a record
    if(request.method == "POST"):    ## if request is post then
        name = request.json["name"]      ## request for name
        number = request.json["number"]   ## request for number
        cursor.execute("INSERT INTO flask_task_db.task_1 values (%s , %s)",(name,number))   ##(%s , %s) this are called place holders like a format in python
        mydb.commit()   ## commit the changes in db
        print("The data is inserted successfully")
        return jsonify(str("data is inserted into database successfuly"))   ## you can see in the postman

## update the record

@app.route("/update",methods=["POST","GET"])
def update():
    if(request.method == "POST"):
        get_name = request.json["get_name"]
        cursor.execute("UPDATE flask_task_db.task_1 SET number = number + 10 WHERE name = %s",(get_name,))
        mydb.commit()
        print("The data is updated successfully")
        return jsonify(str("data is updated into database successfuly"))   ## you can see in the postman


## delete the record in table
@app.route("/delete",methods=["POST","GET"])
def delete():
    if(request.method == "POST"):
        del_name = request.json["del_name"]
        cursor.execute("DELETE FROM flask_task_db.task_1 WHERE name = %s",(del_name,))
        mydb.commit()
        print("The data is deleted  successfully")
        return jsonify(str("data is deleted into database successfuly"))   ## you can see in the postman

## fetch data 

@app.route("/fetch_data",methods=["POST","GET"])
def fetch_data():
    if(request.method=="POST"):
        cursor.execute("SELECT * FROM flask_task_db.task_1")
        l = []                          ## you can see in the postman
        for i in cursor.fetchall():    ## if you need to fetch one data then fetch_one
            l.append(i)
        return jsonify(str(l)) ## you can see in the postman


if __name__ == "__main__":
    app.run(debug=True)
