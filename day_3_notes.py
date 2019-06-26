# Write a function that takes a 2D binary array and returns the number of 1
#   islands. An island consists of 1s that are connected to the north,
#   south, east or west. 

# For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)
      
def island_counter(matrix):
    # Create a visited matrix
    visited = []
    # Create each cell in the matrix to have values of 'False'
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    island_count = 0
    # Walk through each cell in the matrix
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            # If it has not been visited...
            if not visited[y][x]: # 'not visited' should => False
                # If we reach a '1' in a cell...
                if matrix[y][x] == 1:
                    # Do a DFT and mark the 'island' as visited
                    visited = dft(x, y, matrix, visited)
                    # Increment the counter by one
                    island_count += 1
    print(island_count)
    return island_count
            
def dft(x, y, matrix, visited):
    # Create a Stack() to store cells to visit
    s = Stack() 
    # Push the starting coordinates (a tuple; immutable) into the Stack; FIFO
    s.push((x, y))
    # While the stack is NOT empty...
    while s.size() > 0:
        # Pop off the first cell of the Stack() and set it equal to a variable
        current_cell = s.pop()
        x = current_cell[0]
        y = current_cell[1]
        if not visited[y][x]:
            visited[y][x] = True
            for neighbor in get_neighbors((x, y), matrix):
                s.push(neighbor) # Add the vertex (the tuple) to the Stack()
    return visited
  
def get_neighbors(vertex, graph_matrix):
    x = vertex[0]
    y = vertex[1]
    neighbors = []
    # Check North for any values of "1"
    if y > 0 and graph_matrix[y - 1][x] == 1:
        neighbors.append((x, y - 1))
    # Check South for any values of "1"
    #   Must be "len(graph_matrix) - 1" b/c you'll only be able to check for "1" values #   in a South direction up to the 2nd to last item b/c the last item will have no
    #   values South of it to look for.
    if y < len(graph_matrix) - 1 and graph_matrix[y + 1][x] == 1:
        neighbors.append((x, y + 1))
    # Check East for any values of "1"
    if x < len(graph_matrix[0]) - 1 and graph_matrix[y][x + 1] == 1:
        neighbors.append((x + 1, y))
    # Check West for any values of "1"
    if x > 0 and graph_matrix[y][x - 1] == 1:
        neighbors.append((x - 1, y))
    return neighbors
        

island_counter(islands) # returns 4