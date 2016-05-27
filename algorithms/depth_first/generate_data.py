'''
Created on Apr 19, 2016

@author: mcandas
'''

num_depth = 4
num_leaf = 4

tree = list()
active_nodes = list()
active_nodes.append('node1')


for depth in range(1,num_depth):
    #print ('depth', depth)
    #print ('active nodes', active_nodes)
    new_nodes = list()
    for n in active_nodes: 
        #print ('active node', n)       
        for j in range(1,num_leaf):
            new_node = n + str(j)
            tree.append([n,new_node])
            new_nodes.append(new_node)
    #print ('tree', tree)
    active_nodes = new_nodes
    
print ('size :', len(tree), tree)
            
       