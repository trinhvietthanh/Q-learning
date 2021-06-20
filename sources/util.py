from sources.Q_learning import Q_learning


def run(lr, gamma, goal, graph):
    Q_learn = Q_learning(len(graph.nodes), len(graph.nodes), goal, lr, graph, gamma)
    Q_learn.learn(0.5, 500)
    return Q_learn.result()
