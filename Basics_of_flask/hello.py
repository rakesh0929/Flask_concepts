from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>hello</h1>"

'''
safe     ## make the safe and stong html page
capitalize
lower
upper
title
trim --- >  remove the spaces at the end 
striptags
'''
@app.route("/home_page")
def render_page():
    admin_name = "Rakesh"

    stuff = "This is some of the <strong> strong </strong> tag"
    ## safe filter and then if you need to remove the safe tag in the html then you have to use striptags

    favourate_pizza = ["Peporani","cheese","corn","chicken","veg","Mushroom",20]

    return render_template('index.html',admin_name=admin_name,suff=stuff,favourate_pizza = favourate_pizza)


@app.route("/user/<name>")
def user(name):
    return render_template('user.html',user_name=name)


if __name__ == "__main__":
    app.run(debug=True,port=2000)


