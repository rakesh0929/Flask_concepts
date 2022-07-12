## custom error pages



from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>hello</h1>"

@app.route("/home_page")
def render_page():


    stuff = "This is some of the <strong> strong </strong> tag"
    ## safe filter and then if you need to remove the safe tag in the html then you have to use striptags

    admin_name = "Rakesh"

    favourate_pizza = ["Peporani","cheese","corn","chicken","veg","Mushroom",20]

    return render_template('index.html',admin_name=admin_name,suff = stuff, favourate_pizza = favourate_pizza)

@app.route("/user/<name>")
def user(name):
    return render_template('user.html',user_name=name)


## invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html') , 404


## internal surver url
@app.errorhandler(500)
def page_not_found(e):
    return render_template('error_500.html') , 500


if __name__ == "__main__":
    app.run(debug=True,port=2001)