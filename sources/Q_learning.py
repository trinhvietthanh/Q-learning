import numpy as np
import pandas as pd
import random as rd

class Q_learning:
    def __init__(self, states, action, goal, lr, graph, gamma=0.8):
        self.R = np.matrix(np.zeros(shape=(states, action)))# reward table  
        self.Q_table = np.matrix(np.zeros(shape=(states, action)))
        self.Q_table -= 100
        self.states = states
        self.gamma = gamma
        self.lr = lr 
        self.goal = goal
        self.G = graph
        self.addReward()
        self.addEge()
    
    def addEge(self):
        for node in self.G.nodes:
            for x in self.G[node]:
                self.Q_table[node, x] = 0
                self.Q_table[x, node] = 0

    def addReward(self):
        self.R-=100
        print("start")
        print(self.states)
        print(self.goal)
        for node in self.G[self.goal]:
            self.R[node, self.goal] = 100
        for node in self.G.nodes:
            for x in self.G[node]:
                if node != self.goal:
                    self.R[x, node] = -self.G[node][x]['weight']
                    if x != self.goal:  
                        self.R[node, x] = -self.G[node][x]['weight']

    def result(self):
        return self.Q_table

    def select_action(self, start, er):
        random_value = rd.uniform(0, 1)
        if random_value < er:
            sample = self.G[start]
        else: 
            sample = np.where(self.Q_table[start,]==np.max(self.Q_table[start,]))[1]
        next_node = int(np.random.choice(sample,1))
        return next_node
    
    def UpdateQTable(self,node1, node2):
        max_index = np.where(self.Q_table[node2,] == np.max(self.Q_table[node2,]))[1]
        if max_index.shape[0] > 1:
            max_index = int(np.random.choice(max_index, size=1))
        else:
            max_index = int(max_index)
        max_value = self.Q_table[node2, max_index]
        self.Q_table[node1, node2] = int((1-self.lr)*self.Q_table[node1, node2] + self.lr*(self.R[node1, node2] + self.gamma* max_value))
    
    def learn(self,er, episodes):
        for i in range(episodes):
            start = np.random.randint(0, self.states-1)
            next_node = self.select_action(start, er)
            self.UpdateQTable(start, next_node)