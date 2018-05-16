from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:virgin0071@localhost/flask_database'
db = SQLAlchemy(app)

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contactformpost', methods=["GET", "POST"])
def contactformpost():
    user = User(name=request.form['Name'], email=request.form['Email'], message=request.form['Message'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/allcontacts')
def allcontacts():
    all = User.query.all()
    return render_template('allcontacts.html', incomplete=all)
   

if __name__ == '__main__':
    app.run(debug=True)