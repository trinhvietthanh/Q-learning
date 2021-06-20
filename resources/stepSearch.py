from flask_restful import Resource
import numpy as np
from sources.util import run
from sources.env import G
import json

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)

def getPath(begin, end):
    Q = run(0.8, 0.8, 10, graph=G)
    path = [begin]
    next_node = np.argmax(Q[begin,])
    path.append(next_node)
    while next_node != end:
        next_node = np.argmax(Q[next_node,])
        path.append(next_node)
    return path

class StepSearch(Resource):
    def get(self, begin, end):
        path = getPath(begin, end)
        return json.dumps(path, cls=NpEncoder)
