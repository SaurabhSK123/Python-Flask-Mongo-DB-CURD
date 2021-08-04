from flask import Flask
from main import app
from main import routes



if __name__== "__main__":
    app.run(port=5555, debug=True)