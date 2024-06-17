from flask import Flask,url_for
from api import api

app = Flask(__name__)
app.register_blueprint(api,url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)