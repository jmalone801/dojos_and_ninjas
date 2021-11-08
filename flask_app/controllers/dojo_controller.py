from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask import render_template,request,redirect,sessions


@app.route("/")
def home_route():
    return redirect("/dojo")

@app.route('/dojo')
def all_dojos():
    dojo = Dojo.all_dojos()
    return render_template('dojo.html', dojo = dojo)

@app.route('/create_dojo',methods=['POST'])
def create_dojo():
    data = {
        "name": request.form["name"]
    }
    Dojo.create_dojo(data)
    return redirect("/dojo")

@app.route("/new_ninja")
def new_ninja():
    dojos = Dojo.all_dojos()
    return render_template("new_ninja.html", dojos=dojos)

