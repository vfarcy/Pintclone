# video at https://www.youtube.com/watch?v=2geC50roans
# tutorial done until 17"40'

from flask import Flask
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Text


app = Flask(__name__, static_url_path='')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pin.db'

db = SQLAlchemy(app)


class Pin(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(Text, unique=False)
    image = Column(Text, unique=False)


db.create_all()

api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(Pin, methods=['GET', 'POST', 'DELETE', 'PUT'])
# Connect to http://127.0.0.1:5000/api/pin !

app.debug = True


@app.route('/')
def index():
    return app.send_static_file("index.html")


app.debug = True

if __name__ == '__main__':
    app.run()
