from flask import flask 
from db import db

app = flask(__name__)
app.config['SQLACHYEMY_DATABASE_URI']
db.init_app(app)

if_name_ == '_main_':
   app.run(debug=True)