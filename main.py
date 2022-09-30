from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'orgins':"*"}})

@app.route('/',methods=['GET'])
def greetings():
    return('Hello world!')

@app.route('/shark',methods=['GET'])
def shark():
    return('Shark!')

MOVIES = [
    
    {
        'id': uuid.uuid4().hex,
        'title':'Titanic',
        'genre':'love',
        'watched': True,
    },
    {
        'id': uuid.uuid4().hex,
        'title':'The Truman Show',
        'genre':'fiction',
        'watched': False,
    },
    {
        'id': uuid.uuid4().hex,
        'title':'Letters of love',
        'genre':'love',
        'watched': False,
    },
    {
        'id': uuid.uuid4().hex,
        'title':'The Silence of the Lambs',
        'genre':'horror',
        'watched': False,
    },
    {
        'id': uuid.uuid4().hex,
        'title':'Forrest Gump',
        'genre':'love',
        'watched': True,
    }
]

# The Get and Post route handler
@app.route('/movies', methods=['GET','POST'])
def all_movies():
    response_object = {'status':'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        MOVIES.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'watched': post_data.get('watched')})
        response_object['message'] = 'Movie Added!'
    else:
        response_object['movies'] = MOVIES
    return jsonify(response_object)

# The PUT and DELETE route handler
@app.route('/movies/<movie_id>', methods = ['PUT','DELETE'])
def single_movie(movie_id):
    response_object = {'status': 'success'}
    if request.method == "PUT":
        post_data = request.get_json()
        remove_movie(movie_id)
        MOVIES.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'watched': post_data.get('watched')
        })
        response_object['message']='Movie Updated !'
    if request.method == "DELETE" :
        remove_movie(movie_id)
        response_object['message'] = 'Movie removed !'
    return jsonify(response_object)

# Removing the movie to update
def remove_movie(movie_id):
    for movie in MOVIES:
        if movie['id'] == movie_id:
            MOVIES.remove(movie)
            return True
    return False       
  

if __name__=="__main__":
    app.run(debug=True)