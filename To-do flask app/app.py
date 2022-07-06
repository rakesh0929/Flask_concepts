from datetime import datetime
from flask import Flask, redirect , render_template, request
# https://flask.palletsprojects.com/en/1.1.x/quickstart/
from flask_sqlalchemy import SQLAlchemy
from pkg_resources import to_filename
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application
import sqlalchemy


app = Flask(__name__)
#  https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

class Todo(db.Model):
    Sno = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200),nullable=False)
    desc = db.Column(db.String(500),nullable=False)
    data_created = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f'{self.Sno} - {self.title}'

     

@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method == 'POST':
        title = request.form["title"]
        desc = request.form["desc"]

        todo = Todo(title = title,desc = desc)
        db.session.add(todo)
        db.session.commit()
    allTodo = Todo.query.all()
    # print(allTodo)
    return render_template('index.html',allTodo=allTodo)  ## dispaly all todo in the web application

@app.route('/about')
def Products():
    return render_template("aboutpage.html")

@app.route('/update/<int:Sno>',methods=['GET','POST'])
def Update(Sno):
    if request.method == "POST":
            title = request.form["title"]
            desc = request.form["desc"]

            todo_updated = Todo.query.filter_by(Sno=Sno).first()
            todo_updated.title = title
            todo_updated.desc = desc

            db.session.add(todo_updated)
            db.session.commit()
            return redirect("/")
    
        # db.session.commit()
    todo_updated = Todo.query.filter_by(Sno=Sno).first()
    return render_template('update.html',todo_updated=todo_updated)
    

@app.route('/delete/<int:Sno>') # https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/?highlight=delete
def delete(Sno):
    todo = Todo.query.filter_by(Sno=Sno).first()
    db.session.delete(todo)
    db.session.commit()

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True,port=1234)

