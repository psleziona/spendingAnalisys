import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('SPENDING_DB')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'rachunek'