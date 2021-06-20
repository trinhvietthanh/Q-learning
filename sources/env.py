import networkx as nx

edges = []


def convertToEnv(node1, node2, weight):
    edges.append((node1, node2, {"weight": weight}))
    return edges
# edges = [(0,4, {"weight": 3.5}),(4,0, {"weight": 3.5}),(0,3, {"weight": 3.5}),(3,0, {"weight": 3.5})
# ,(1,2, {"weight": 4.6}), (2,1, {"weight": 4.6}), (1,4, {"weight": 10.5}), (4,1, {"weight": 10.5}), 
# (1,8, {"weight": 3.5}), (8,1, {"weight": 3.5}), (1,9, {"weight": 4.5}), (7, 9, {"weight": 4.5}), 
# (9, 7, {"weight": 4.5}),(7,5, {"weight": 5.5}),(5,7, {"weight": 5.5}), (9,1, {"weight": 4.5}) ,(3,5, {"weight": 8.5}),
# (5, 3, {"weight": 8.5}), (6, 4, {"weight": 1.5}), (4,6, {"weight": 1.5}), (3, 10, {"weight": 2.5}), (10, 3, {"weight": 2.5}), 
# (4, 10, {"weight": 6.5}), (10, 4, {"weight": 6.5}), (4, 9, {"weight": 5.5}), (9 , 4, {"weight": 5.5})]
G =  nx.Graph()
G.add_edges_from(edges)

