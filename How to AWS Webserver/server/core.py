from flask import Flask,render_template
from flask import request
import os

app = Flask('__name__', template_folder='templates')

@app.route("/home")
def HomePage():
    return render_template("home.html")
    
@app.route("/basic-JavaScript")
def BasicJavaScript():
    return render_template("basic-JavaScript.html")

@app.route("/basic-css")
def basicCSS():
    return render_template("basic-css.html")
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)
    app.run(debug=True) #can alter host and port number here. Right now the default host is localhost and port is 5000
