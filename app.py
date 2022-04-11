from flask import Flask, render_template, request
import math
import numpy

app = Flask(__name__, template_folder='template',static_folder='static')

@app.route("/", methods=["POST", "GET"])

def calculate():
    x1=""
    if request.method=='POST' and "T(t)" in request.form and "T0" in request.form and "t" in request.form and "Ts" in request.form:
        Tt = float(request.form.get("T(t)"))
        T0 = float(request.form.get("T0"))
        t = float(request.form.get("t"))
        Ts = float(request.form.get("Ts"))
        Tb = 37

        k = (math.log((Tt-Ts)/(T0-Ts)))
        k1 = k/t*-1

        x = (math.log((T0-Ts)/(Tb-Ts)))
        x1 = round(x/k1*-1)
    return render_template('index.html',x1=x1)
