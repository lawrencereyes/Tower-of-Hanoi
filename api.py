from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from resource.errors import errors

import os, sys, json
import markdown

sys.path.append(".")

from tower_of_hanoi import TowerOfHanoi
game = TowerOfHanoi()

app = Flask(__name__)
api = Api(app, errors=errors)

parser = reqparse.RequestParser()
parser.add_argument('from_rod', type=str, required=True, help='The rod that has the disk we want to move is required')
parser.add_argument('to_rod', type=str, required=True, help='The rod that will recieve the disk is required')

@app.route('/')
def index():
    """Present the Tower of Hanoi Game Documentation"""
    
    #Open the README file
    with open('README.md', 'r') as markdown_file:

        #Read the content of the file
        content = markdown_file.read()

        #Convert to HTML
        return markdown.markdown(content)

class State(Resource):
    def get(self):

        state = game.getState()

        winner = False

        #Check if all the disks have been move to another rod in order
        if state['b'] == [1, 2, 3, 4]:
            winner = True
        elif state['c'] == [1, 2, 3, 4]:
            winner = True

        return {'current_state': state,'winner': winner, 'status': 200}, 200

class MoveDisk(Resource):
    def post(self):
        args = parser.parse_args()
        from_rod = args['from_rod']
        to_rod = args['to_rod']

        a = game.moveDisk(from_rod, to_rod)

        if a == None:
            return {'message': 'You have made a move. Check the state.', 'status': 200}, 200
        elif a:
            return a, a['status']

class NewGame(Resource):
    def get(self):
        game.newGame()

        return {'message': 'You have started a new game the game.', 'status': 200}, 200

class Restart(Resource):
    def get(self):
        game.restart()

        return {'message': 'You have restarted the game.', 'status': 200}, 200

#All routes (except index and documentation)
api.add_resource(State, '/game/state')
api.add_resource(MoveDisk, '/game/move')
api.add_resource(NewGame, '/game/new')
api.add_resource(Restart, '/game/restart')

if __name__ == "__main__":
    app.run(debug=True)