# app.py - default that Flask looks for

from flask import Flask, jsonify, request # Must be capital F for named import!
from flask_cors import CORS
from werkzeug import exceptions

# port (default is 5000)

# server instance
app = Flask(__name__)
CORS(app) # Add cross origin policy

#  security (some in-built functionality exists)

# logic for handling requests
@app.route('/') # By default responds to "get"
def welcome():
    return 'Welcome to Flask'

@app.route('/players', method=['GET', 'POST'])
def players_handler():
    if request.method == 'GET':
        players = ['Mark Selby', 'Shaun Murphy', 'Ding Junhui']
        return jsonify(players), 200
    elif request.method == 'POST':
        data = request.json
        return f"You made a player with {data['name']}", 201

@app.route('/players/<int:player_id>')
def player_handler(player_id):
    return f'You chose player with id {player_id}'

@app.errorhandler(exceptions.NotFound)
def handle_not_found(err):
    return jsonify({"message": f'{err}'})

@app.errorhandler(exceptions.InternalServerError)
def handle_internal_server_error(err):
    return jsonify({"message": "It's not you, it's us"})

# start the server listening
if __name__ == '__main__': # Only runs when we run app.py
    app.run(debug=True) # Equivalent to app.listen in JS

# Run above with 'flask run'