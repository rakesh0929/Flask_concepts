from flask import Flask,request,jsonify

app = Flask(__name__)

# app.config['sql_data_base'] = 'mysql://root:Rakesh@12345678@localhost:3307/db_name'

@app.route('/abc',methods=['POST','GET'])
def add():
    if(request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a+b
        return jsonify(str(result))


@app.route('/cde',methods=['POST','GET'])
def add_():
    if(request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a*b
        return jsonify(str(result))



if __name__ == "__main__":
    app.run(debug=True)






