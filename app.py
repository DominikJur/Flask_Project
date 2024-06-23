from flask import Flask, request, jsonify, render_template

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

@app.route('/zagadnienie')
def zagadnienie():
    return render_template("zagadnienie.html")

if __name__ == '__main__':
    app.run(debug=True)