from flask import Flask, render_template, redirect, url_for,request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://masterDB:qwerty123@cluster0.1efsd.mongodb.net/simpleTodoApp?retryWrites=false&w=majority"
mongo = PyMongo(app)
todos = mongo.db.todos

@app.route("/")
def index():
    saved_todos = todos.find()
    return render_template("index.html", todos=saved_todos)

@app.route("/add", methods=["POST"])
def add_todo():
    new_todo = request.form.get('new-todo')
    todos.insert_one({'task':new_todo, 'completed':False})
    return redirect(url_for('index'))
