from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'contactform'
  uid = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(100))
  email = db.Column(db.String(120), unique=True)
  message = db.Column(db.String(100))
  
  def __init__(self, name,  email, message):
    self.name = name.title()
    self.email = email.lower()
    self.message = message
    