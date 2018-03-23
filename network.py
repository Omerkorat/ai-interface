"""This module defines tools for creating networks which can serve as a backend to 
AI interface. A network can represent any connected structure, such as floor plans, power grid,
tube systems, etc'.
A network is an mXm matrix with m nodes. The value in the i,j cell represents
the connection type between the i-th and j-th nodes, where 0 means no connection.
Some stuff is taken from:
https://www.python-course.eu/graphs_python.php
"""

import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame


class Network:
    
    def __init__(self, m=None, connections_space={0,1}, node_labels=None, is_symmetric = True):
        
        """
        :param m: number of nodes.
        :param connections_space: Optional, defaults to {0,1}.  an object that checks for inclusion in the space of allowed
        connection strength values. For example, the set {0,1} defines a binary connection 
        space. The predicate (lambda x: isinstance(x,int)) defines the space of natural numbers.
        :param nodel_labels: names for nodes. Optional, defaults to index numbers of nodes.
        :param is_symmetrical: are connections in the network symmetrical. Asymmetric networks not yet implemented.
        """
        
        if m is None and node_labels is None:
            raise ValueError("At least one of m and node_labels must be given.")
        if not is_symmetric:
            raise NotImplementedError("Asymmetric networks not yet implemented.")
        assert all([isinstance(x,float) or isinstance(x,int) for x in connections_space]), "Connection space must be defined over the type of int or float."
        if node_labels is None:
            node_labels = list(range(m))
        if m is None:
            m = len(node_labels)
        assert m == len(node_labels), "m must equal number of node labels."
        
        self.connections_space = connections_space
        self.nodes = node_labels
        
        if any([isinstance(x,float) for x in connections_space]):
            self.dtype = float
        else:
            self.dtype = int 
        self.mat = np.zeros((m,m),dtype=self.dtype)
        self.n_nodes = len(self.nodes)
        
    def connect(self, i,j,strength=1):
        """Establish a connection with given strength between two nodes with indexes i,j."""
        if strength not in self.connections_space:
            raise ValueError("Connection strength must be in %s" % str(self.connections_space))
        self.mat[i,j] = strength
    
    def __getitem__(self, item):
        return self.mat[item]
    
    def __setitem__(self, *args):
        raise ValueError("To establish connections in the network call Network.connect.")
    
    def get_names(self, nodes):
        """Maps a list of node indexes to their labels in the graph."""
        return list(map(self.nodes.__getitem__,nodes))
        
    
    def find_path(self, start_node, end_node):
        """ find a path from start_node to end_node 
                in network. Returns indexes of node labels.
                Nodes can be given either as index or names."""
        path = self.find_path_helper(start_node, end_node)
        if path is None:
            return path
        return self.get_names(path)
    
    def find_path_helper(self, start_node, end_node, path=None):
            if not isinstance(start_node,int):
                start_node = self.nodes.index(start_node)
            if not isinstance(end_node,int):
                end_node = self.nodes.index(end_node)
            
            if path == None:
                path = []
            path = path + [start_node]
            if start_node == end_node:
                return path
            
            for node in range(self.n_nodes):
                if self[start_node][node] and node not in path:
                    extended_path = self.find_path_helper(node, 
                                                   end_node, 
                                                   path)
                    if extended_path: 
                        return extended_path
            return None
    
    def find_all_connected_nodes(self, node):
        """Return a list of all nodes connected to given node."""
        return [other for other in self.nodes if self.find_path(node, other)]
        
    def find_all_paths(self, start_node,end_node):
        """ find all paths from start_node to 
            end_node in graph.
            Nodes can be given either as index or names."""
        paths = self.find_all_paths_helper(start_node, end_node)
        return [self.get_names(path) for path in paths]
    
    def find_all_paths_helper(self, start_node, end_node, path=[]):
        
        if not isinstance(start_node,int):
            start_node = self.nodes.index(start_node)
        if not isinstance(end_node,int):
            end_node = self.nodes.index(end_node)
        
        path = path + [start_node]
        if start_node == end_node:
            return [path]
        paths = []
        for node in range(self.n_nodes):
            
            if self[start_node][node] and node not in path:
                extended_paths = self.find_all_paths_helper(node, 
                                                     end_node, 
                                                     path)
                for p in extended_paths: 
                    paths.append(p)
        return paths            
    
    def __str__(self):
        return DataFrame(self.mat,index=self.nodes,columns=self.nodes,dtype=self.dtype).to_string()
        
def test():
    
    net = Network(node_labels=['a','b','c','d','e','f','g'])
    net.connect(0,1)
    net.connect(1,2)
    net.connect(0,3)
    net.connect(3,4)
    net.connect(4,2)
    
    print(net.find_path(0,2))
    print(net.find_path('b','c'))
    print(net.find_all_paths(0,2))

if __name__ == '__main__':
    test()