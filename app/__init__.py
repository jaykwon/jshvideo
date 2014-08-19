from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.httpauth import HTTPDigestAuth

app = Flask(__name__, static_url_path='')
app.config.from_object('config')
db = SQLAlchemy(app)
auth = HTTPDigestAuth()


from app.routes import index
