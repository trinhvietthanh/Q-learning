from flask_restful import Resource
from sources import env
from networkx.readwrite import json_graph
from sources.util import run
import json

class GraphDefault(Resource):
    def get(self):
       result = json_graph.node_link_data(env.G)
       return result

class Q_table(Resource):
    def get(self):
        res = run(0.8, 0.8, 10, graph=env.G)
        res = res.tolist()
        return json.dumps(res)



