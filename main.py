# this is a simple API to show the data of artist

from flask import Flask, request, jsonify, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import json

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# artist Class/Model
class artist(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True)
  art_style = db.Column(db.String(200))
  location = db.Column(db.String(200))
  age = db.Column(db.Float)
  experience = db.Column(db.Integer)

  def __init__(self, name, art_style, location, age, experience):
    self.name = name
    self.art_style = art_style
    self.location = location
    self.age = age
    self.experience = experience

# artist Schema
class artistSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'art_style', 'location', 'age', 'experience')

# Init schema
artist_schema = artistSchema()
artists_schema = artistSchema(many=True)

# render  main page
@app.route('/')
def home_page():
  # return '<h1>hello</h1>'
  return render_template('index.html')

# add artist details
@app.route('/artists', methods=['POST'])
def add_artist():
  # name = request.form['name']
  # art_style = request.form['art_style']
  # location = request.form['location']
  # age =int(request.form['age'])
  # experience = int(request.form['experience'])
  #
  # new_artist = artist(name, art_style, location, age, experience)
  #
  # db.session.add(new_artist)
  # db.session.commit()

  # return jsonify(request.form)
  print(request.get_json())
  return request.get_json()


# Get All artist
@app.route('/artists', methods=['GET'])
def get_artists():
  all_artists = artist.query.all()
  result = artists_schema.dump(all_artists)
  return jsonify(result)

# Get Single artist
@app.route('/artists/<id>', methods=['GET'])
def get_artist(id):
  ind_artist = artist.query.get(id)
  return artist_schema.jsonify(ind_artist)


# Update a artist
@app.route('/artists/<id>', methods=['PUT'])
def update_artist(id):
  ind_artist = artist.query.get(id)

  name = request.json['name']
  art_style = request.json['art_style']
  location = request.json['location']
  age = request.json['age']
  experience = request.json['experience']

  ind_artist.name = name
  ind_artist.art_style = art_style
  ind_artist.location = location
  ind_artist.age = age
  ind_artist.experience = experience

  db.session.commit()

  return artist_schema.jsonify(ind_artist)

# Delete artist
@app.route('/artists/<id>', methods=['DELETE'])
def delete_artist(id):
  ind_artist = artist.query.get(id)
  db.session.delete(ind_artist)
  db.session.commit()

  return artist_schema.jsonify(ind_artist)

# Run Server
if __name__ == '__main__':
  app.run(debug=True)

  # >> > from main import db
  # >> > db.create_all()
  # >> > exit()
