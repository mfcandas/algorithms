'''
Created on Apr 28, 2016

@author: mcandas
'''

import pandas as pd
import matplotlib.pyplot as plt



def plot_apartment(L_input, L_cv):
    fig = plt.figure()
    
    ax1 = fig.add_subplot(2,1,1)
    
    ax1.axis([0, 20, 0, 10])
    for ap in L_input:
        l_x = [ap[0],ap[0],ap[1],ap[1]]
        l_y = [0,ap[2],ap[2],0]
        ax1.plot(l_x,l_y, 'r')
    plt.xticks(range(0,20,1))
    plt.yticks(range(0,10,1))
    plt.grid()
    
    ax2 = fig.add_subplot(2,1,2)
    l_x = [c[0] for c in L_cv]
    l_y = [c[1] for c in L_cv]
    ax2.plot(l_x, l_y)
    #plt.axis([0, max(l_x)+1, 0, max(l_y)+1])
    
    #===========================================================================
    # fig2 = plt.figure()
    # ax1 = fig2.add_subplot(2,1,1)
    # 
    # ax1.axis([0, 20, 0, 10])
    # for ap in L_input:
    #     l_x = [ap[0],ap[0],ap[1],ap[1]]
    #     l_y = [0,ap[2],ap[2],0]
    #     ax1.plot(l_x,l_y, 'r--')
    # 
    # ax2 = fig2.add_subplot(2,1,2)
    # l_x = [c[0] for c in L_cv]
    # l_y = [c[1] for c in L_cv]
    # ax2.plot(l_x, l_y)
    # ax2.axis([0, 20, 0, 10])
    #===========================================================================
    ax2.axis([0, 20, 0, 10])
    plt.xticks(range(0,20,1))
    plt.yticks(range(0,10,1))
    plt.grid()
    plt.show()   


DF_input__x1_x2_y   = pd.DataFrame()
DF_input__x1_x2_y   = pd.read_table("./data/hi_rise_data.csv", sep=',')
print (DF_input__x1_x2_y)

L_input__x1_x2_y = DF_input__x1_x2_y.values.tolist()
L_all_x__x = [a[0] for a in L_input__x1_x2_y] + [a[1] for a in L_input__x1_x2_y]
L_all_x__x.sort()

# plot_solution(L_input__x1_x2_y)

# initial height 
p_height = 0  
L_city_view = list()
D_city_view = dict()

def all_in_one_step(L_input__x1_x2_y):
    for x in L_all_x__x:
        print (x)
        # get list of buildings at this Coordinate
        L_buildings = [l for l in L_input__x1_x2_y if x>=l[0] and x<=l[1]]
        print (L_buildings)
        
        p_height = max([l[2] for l in L_buildings])
        if (p_height==L_city_view[-1][-1]):
            pass
        else:
            L_city_view.append([x,L_city_view[-1][-1]])
            L_city_view.append([x,p_height])
        print (L_city_view)
    

def one_by_one(L_input__x1_x2_y):
    # add base view at heiht = 0
    p_city_left_x = min(L_all_x__x)
    p_city_right_x = max(L_all_x__x)

    D_city_view = {x: 0 for x in range(p_city_left_x,p_city_right_x+1) }
    
    for tower in L_input__x1_x2_y:
        for x in range(tower[0],tower[1]+1):
            D_city_view[x] = max(tower[2],D_city_view[x])
                
    
    L_city_view = [[x, D_city_view[x]] for x in  D_city_view]  
    print (D_city_view)
    print (L_city_view)   
    return L_city_view 
    

plot_apartment(L_input__x1_x2_y, one_by_one(L_input__x1_x2_y))
 