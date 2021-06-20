from flask import Flask, render_template, request
from flask_restful import Api
from resources.graphDefault import GraphDefault, Q_table
from resources.stepSearch import StepSearch
import mimetypes
import random as rd
import sources.env as env

app = Flask(__name__)
api = Api(app)

mimetypes.add_type('application/javascript', '.js')


@app.route("/get-default-graph", methods=['POST', 'GET'])
def getGraph():
    return env.G

@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template("index.html")
@app.route("/set-graph", methods=['POST', 'GET'])
def setGraph():
    data =  request.data

    # graph = data['graph']
    end = request.form.get('end')
    start = request.form.get('start')
    graph = request.form.get('graph')
    print(graph,end)
    for i in graph:
        w = rd.randint(0,22)
        print(i)
        # env.convertToEnv()
    return "OK"

api.add_resource(GraphDefault,'/api/get-graph')
api.add_resource(Q_table, '/api/get-q-table')
api.add_resource(StepSearch, '/api/path/<int:begin>/<int:end>', endpoint='get-path')

if __name__ == '__main__':
    app.run(port=5050, debug=True)