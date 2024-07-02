from flask import Flask, request, jsonify, render_template
import numpy as np
from src.utils import plot_log
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index')
def back_to_index():
    return render_template("index.html")

@app.route('/authors')
def authors():
    return render_template("authors.html")

@app.route('/zagadnienie', methods=['POST', 'GET'])
def zagadnienie():
    base = np.e
    xmin = 0.001
    xmax = 10.001

    if request.method=='POST':
        try:
            base = float(request.form['base'])
            xmin = float(request.form["xmin"])
            xmax = float(request.form["xmax"])
        except Exception as e:
            return render_template("zagadnienie.html", plot=plot_log(base=base, xmin=0.001, xmax=10.001))
    plot = plot_log(base, xmin, xmax)
        
    return render_template("zagadnienie.html", plot=plot)


if __name__ == '__main__':
    app.run(debug=True)