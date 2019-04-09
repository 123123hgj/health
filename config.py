from datetime import timedelta
import os
uri = os.path.join(os.path.dirname(__file__), 'site.db')
SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
# SQLALCHEMY_DATABASE_URI = 'sqlite:///'+r'C:\Users\Administrator\Documents\Tencent Files\690631890\FileRecv\Health_Web1\site.db'
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+uri
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
PERMANENT_SESSION_LIFETIME = timedelta(days=7)

