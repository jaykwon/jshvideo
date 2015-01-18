import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

VIDEOS_DIRECTORY = 'app/static/media/videos'
FRAMES_DIRECTORY = 'app/static/media/frames'

TOKEN_SECRET = os.environ.get('SECRET_KEY') or 'JWT Token Secret String'
FACEBOOK_SECRET = os.environ.get('FACEBOOK_SECRET') or 'Facebook Client Secret'
GITHUB_SECRET = os.environ.get('GITHUB_SECRET') or 'GitHub Client Secret'
FOURSQUARE_SECRET = os.environ.get('FOURSQUARE_SECRET') or 'Foursquare Client Secret'
GOOGLE_SECRET = os.environ.get('GOOGLE_SECRET') or 'Google Client Secret'
LINKEDIN_SECRET = os.environ.get('LINKEDIN_SECRET') or 'LinkedIn Client Secret'
TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY') or 'Twitter Consumer Secret'
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET') or 'Twitter Consumer Secret'
TWITTER_CALLBACK_URL = os.environ.get('TWITTER_CALLBACK_URL') or 'Twitter Redirect URI'
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///app.db'