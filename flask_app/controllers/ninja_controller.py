from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask import render_template,request,redirect,sessions

@app.route('/create_ninja',methods=['POST'])
def create_ninja():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    Ninja.create_ninja(data)
    return redirect("/")

@app.route('/dojo_ninjas/<int:id>')
def dojo_ninjas(id):
    data = {
        "id" : id
    }
    dojo_ninjas = Dojo.dojo_ninjas_join(data)
    return render_template("dojo_ninjas.html", dojo_ninjas = dojo_ninjas)

