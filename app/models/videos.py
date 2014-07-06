from app import db
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.types import TypeDecorator, VARCHAR
import json


#from flask import Flask
#app = Flask(__name__)
#db = SQLAlchemy(app)

class JSONEncodedDict(TypeDecorator):
    impl = VARCHAR
    def process_bind_param(self, value, dialect):
        if value is not None:
            value = json.dumps(value)
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)
        return value

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    filename = db.Column(db.Text(), unique=True)
    attr = db.Column(JSONEncodedDict())

    def __init__(self, name, filename, attr):
        self.name = name
        self.filename = filename
        self.attr = attr

    def __repr__(self):
        return '<Video %r>' % self.name

if __name__ == '__main__':
    db.create_all()
    video = Video('flame', 'flame.avi', "{'some': 'attrs'}")
    db.session.add(video)
    db.session.commit()
    print "Videos\n---------\n", Video.query.all()
