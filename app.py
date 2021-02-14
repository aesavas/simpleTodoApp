from flask import Flask, render_template, redirect, url_for,request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

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

@app.route("/complete/<oid>")
def complete(oid):
    todo = todos.update_one({'_id': ObjectId(oid)}, {'$set':{'completed':True}})
    return redirect(url_for('index'))

@app.route("/delete-completed")
def deleteCompleted():
    deleted = todos.delete_many({'completed':True})
    return redirect(url_for('index'))

@app.route("/delete-all")
def deleteAll():
    deleted = todos.delete_many({})
    return redirect(url_for('index'))

@app.route("/delete/<oid>")
def deleteSelected(oid):
    deleted = todos.delete_one({'_id':ObjectId(oid)})
    return redirect(url_for('index'))