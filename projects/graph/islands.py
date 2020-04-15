'''
Write a function that takes a 2D binary array and returns the number of 1 islands.
An island consists of 1s that are connected to the north, south, east or west.
For example:
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
island_counter(islands) # returns 4
'''

# islands consist of - connected components
# connected - neighbors (edges)
# directions, nsew (edges)
# 2d array - graph, more or less
# returns (shape of solution) - number of islands

# write a get neighbors function

# how can we find the extent of an island?
# Either of our traversal methods

# How do I explore the larger set?
# loop through and call a traversal if we find an unvisited 1


def island_counter(islands):
    # get shape
    limit = len(islands)
    visited = [[False] * limit] * limit
    island_counter = 0
    # iterate though the 'islands'
    for i in range(limit):
        for j in range(limit):
            if not visited[i][j] and islands[i][j] == 1:
                visited = get_neighbors() # TODO
                island_counter += 1
            else:
                visited[i][j] = True
            
    return island_counter
    # search for an unvisited 1
    # get 1 neighbors
    # add to visited
    # if no more neighbors bo back




def get_neighbors(x, y, limit, visited, islands):
    # get shape of area
    
    # look north
    if x != 0 and islands[x-1][y] == 1:
    # look south
    # look east
    # look west


