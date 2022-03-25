from flask import Flask, render_template, request, jsonify
import math
from numpy import float16

app = Flask(__name__, template_folder='template',static_folder='static')

e = float(2.71828182845)
Ts = int(21)
Tb = int(37)

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")

@app.route("/", methods=["POST", "GET"])
def getvalue():
    Tt = request.form("T(t)", type=int) 
    T0 = request.form("T0", type=int)
    t = request.form("t", type=int)

    k = (math.log((Tt-Ts)/(T0-Ts)))
    k1 = k/t*-1

    x = (math.log((T0-Ts)/(Tb-Ts)))
    x1 = x/k1*-1

    final = {}
    final['status'] = x1

    return jsonify(x1)

if __name__ == "__main__":
    app.run(debug=True)
    