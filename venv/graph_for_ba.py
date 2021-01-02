import networkx as nx
import matplotlib.pyplot as plt
import itertools

H = nx.DiGraph()

axis_labels = ['s1','t1','u1', 'v1']

D_len_node = {}

#Iterate through axis labels
for i in range(0,len(axis_labels)+1):
    #Create edge from empty set
    if i == 0:
        for ax in axis_labels:
            H.add_edge('{}', ax)  # f'{ax}, '
    else:
        #Create all non-overlapping combinations
        combinations = [c for c in itertools.combinations(axis_labels,i)]
        D_len_node[i] = combinations
    #Create edge from len(i-1) to len(i) #eg. pq >>> pqr, pq >>> pqs
    if i > 1:
        for node in D_len_node[i]:
            for p_node in D_len_node[i-1]:
                if set.intersection(set(p_node),set(node)):
                    H.add_edge(''.join(p_node),''.join(node))

#This is manual two options to project tesseract onto 2D plane
# - many projections are available!!
wikipedia_projection_coords = [(0.5,0),(0.85,0.25),(0.625,0.25),(0.375,0.25),
                                (0.15,0.25),(1,0.5),(0.8,0.5),(0.6,0.5),
                                (0.4,0.5),(0.2,0.5),(0,0.5),(0.85,0.75),
                                (0.625,0.75),(0.375,0.75),(0.15,0.75),(0.5,1)]

#Build the "two cubes" type example projection co-ordinates
# half_coords = [(0,0.15),(0,0.6),(0.3,0.15),(0.15,0),
#                (0.55,0.6),(0.3,0.6),(0.15,0.4),(0.55,1)]
# #make the coords symmetric
# example_projection_coords = half_coords + [(1-x,1-y) for (x,y) in half_coords][::-1]
#
# print(example_projection_coords)


def powerset(s):
    ch = itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))
    return [''.join(t) for t in ch]

pos={}
for i,label in enumerate(powerset(axis_labels)):
    if label == '':
       label = '{}'
    pos[label]= wikipedia_projection_coords[i]

#Show Plot
nx.draw(H,pos,with_labels = True,node_shape = 'o', node_color='pink')
plt.show()