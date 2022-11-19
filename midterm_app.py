from flask import Flask
from flask import request
from flask import render_template

webapp = Flask(__name__)

@webapp.route("/")
def main():

    return render_template("index.html")

if __name__ == '__main__':
    webapp.run(host="0.0.0.0", port=5050)