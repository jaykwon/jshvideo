import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

VIDEOS_DIRECTORY = 'app/static/media/videos'
FRAMES_DIRECTORY = 'app/static/media/frames'

SECRET_KEY = ')\xf5\x96\xc7\x8e\xc0|Mt\xca@\xf0s\xfd\xce\xc8\xe1\xf5\xa8V\x973\xcd2'
