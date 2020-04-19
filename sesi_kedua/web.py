# ===========================

# ***************************
# Workshop Python Series Programs 2
# Pemateri      : Hadi Hidayat Hammurabi
# Source Code   : Hadi Hidayat Hammurabi
# Source        : Praxis Academy dan Padekopan Asa Wedomartini
# ***************************

# ***************************
# Author        : Salim Suprayogi
# Sabtu, 18 april 2020
# Pukul 10.00-12.00 WIB
# ***************************

# ===========================

# import flask dan templates
from flask import Flask, render_template

app = Flask("web")
# other metode
# app = Flask("web", template_folder="templates") # nama templatenya

# send data to template
@app.route("/")
def index():
    return "halo hi semua"

# send data to template
@app.route("/hello/<name>")
def hello_by_name(name):
    return render_template("index.html", name=name)

# send data to template
@app.route("/hitung/<int:pertama>/<int:kedua>")
def hello_by_hitung(pertama, kedua):
    hasil = pertama + kedua
    return render_template("index2.html", hasil=hasil)

# route parameter
# /users/3
# /users/100
@app.route("/users/<id>")
def users_by_id(id):
    return f"ini user dengan id {id}"


app.run(debug=True)
