'''
Created on Apr 19, 2016

@author: mcandas
'''
#===============================================================================
# import pandas as pd
# df_data = pd.DataFrame
# df_data = pd.read_table("./data/depth_first_data.csv")
# l_data = df_data.values.tolist()
# print (l_data)
#===============================================================================

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

l_data = tree

# list of paths in depth search
l_tree = list()

# list of nodes in depth search 
l_nodes = list()
l_nodes.append(l_data[0][0])

# each individual path
l_path = list()
l_path.append(l_data[0][0])


cont = 1
while len(l_data): 
    # get list of nodes connected to last active node
    l_arc = [b for (a,b) in l_data if a==l_path[-1]]
    
    if len(l_arc):
        cont = True
        l_path.append(l_arc[0])
        l_nodes.append(l_arc[0])
        #print (l_path)
    else:
        rem_arc = [l_path[-2],l_path[-1]]
        l_data.remove(rem_arc)
        l_tree.append(l_path)
        l_path = l_path[0:-1]
        print (l_tree)
        #print (l_path)

print (l_nodes)