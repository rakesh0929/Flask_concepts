from flask import Flask,request,jsonify
import mysql.connector as connection

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def test():
    get_name = request.args.get("get_name")
    mobile_number =  request.args.get("mobile_number")
    mail_id  = request.args.get("mail_id")
    return "<b><h1>Hey hi guys this is {} and this is my mobile number {} and my mail id {}</b></h1>".format(get_name,mobile_number,mail_id)

# http://127.0.0.1:5000/?get_name=Rakesh&mobile_number=899&mail_id=Rakesh@1234

## featch the data from databse table and print it out in the webpage

@app.route("/get_data")
def featch_data():
    db = request.args.get("db")
    tn = request.args.get("tn")
    try:
        conn = connection.connect(host="localhost",user="root", passwd="Rakesh@12345678",use_pure=True,port=3307,database=db)
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM {}".format(tn))
        data = cur.fetchall()
        conn.commit()
        conn.close()
    except Exception as e:
        return jsonify(str(e))
    return jsonify(str(data))

'''# ## dictionary=True 

# http://127.0.0.1:5000/get_data?db=flask_task_db&tn=task_1 --- > input db name show be alredy present and tn name as well
# "[{'name': 'Rockstar', 'number': 456712}, {'name': 'Rockstar2', 'number': 45}, {'name': 'Rakesh', 'number': 948}]"  ---> output
'''

'''
# http://127.0.0.1:5000/get_data?db=flask_task_db&tn=task_1 --- > input db name show be alredy present and tn name as well
# "[('Rockstar', 456712), ('Rockstar2', 45), ('Rakesh', 948)]"  ---> output
'''

if __name__ == "__main__":
    app.run(debug=True)

