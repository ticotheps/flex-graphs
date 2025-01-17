"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    # Represent a graph as a dictionary of vertices mapping labels to edges
    def __init__(self):
        self.vertices = {}
    # Add a vertex_id to the graph
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    # Add a directed edge to the graph.
    def add_edge(self, vertex_1_id, vertex_2_id):
        if vertex_1_id not in self.vertices:
            self.vertices[vertex_1_id] = set()
        if vertex_2_id not in self.vertices:
            self.vertices[vertex_2_id] = set()
        self.vertices[vertex_1_id].add(vertex_2_id)
        # if vertex_1_id in self.vertices and vertex_2_id in self.vertices:
        #     self.vertices[vertex_1_id].add(vertex_2_id)
        # else:
        #     raise IndexError("That vertex does not exist")
          
    def bft(self, starting_vertex_id):
        # Step 1: Create an empty QUEUE and enqueue the starting_vertex_id
        q = Queue()
        q.enqueue(starting_vertex_id)
        # Step 2: Create a Set() to store visited vertices
        #         NOTE: Sets are a good data structure b/c: they're 
        #               unordered and don't have duplicated items
        visited = set()
        # Step 3: Use a WHILE loop that continues while queue is NOT empty
        while q.size() > 0:
            # Step 4: Dequeue the FIRST vertex [to evaluate] and set it equal
            #         to a variable
            current_vert = q.dequeue()
            if current_vert not in visited:
                # Step 5: If it has NOT been visited, print it and add it 
                #         into the set as an item
                print(current_vert)
                visited.add(current_vert)
                # Step 6: Use a FOR loop that iterates over each of current_vert's
                #         neighbors, adding each one to end of the queue
                for next_vert in self.vertices[current_vert]:
                    q.enqueue(next_vert)
        
    def dft(self, starting_vertex_id):
        # Step 1: Create an empty STACK and push the starting_vertex_id
        s = Stack()
        s.push(starting_vertex_id)
        # Step 2: Create a Set() to store visited vertices
        #         NOTE: Sets are a good data structure b/c: they're 
        #               unordered and don't have duplicated items
        visited = set()
        # Step 3: Use a WHILE loop that continues while stack is NOT empty
        while s.size() > 0:
            # Step 4: Pop the FIRST vertex [to evaluate] and set it equal
            #         to a variable
            current_vert = s.pop()
            if current_vert not in visited:
                # Step 5: If it has NOT been visited, print it and add it 
                #         into the set as an item
                print(current_vert)
                visited.add(current_vert)
                # Step 6: Use a FOR loop that iterates over each of current_vert's
                #         neighbors, adding each one to end of the queue
                for next_vert in self.vertices[current_vert]:
                    s.push(next_vert)
                    
    def dft_recursive(self, starting_vertex_id, visited=None):
        # Step 1: Check to see if a set() to store visited vertices exists.
        #         If not, create one.
        if visited is None:
            visited = set()
        # Step 2: Check to see if starting_vertex_id is in the set(). 
        if starting_vertex_id not in visited:
            # Step 3: If not, print it and add it to the set().
            print(starting_vertex_id)
            visited.add(starting_vertex_id)
            # Step 4: Use a FOR loop that iterates over each of starting_vertex_id's
            #         neighbors, calling the dft_recursive() method on each one
            for neighbor in self.vertices[starting_vertex_id]:
                self.dft_recursive(neighbor, visited)
                
    def bfs(self, starting_vertex_id, destination_vertex_id):
        # Step 1: Create an empty QUEUE and enqueue the starting_vertex_id,
        #         WITHIN an array, to the end of the queue (b/c we're 
        #         storing PATHS this time, not "vertices")
        q = Queue()
        q.enqueue( [starting_vertex_id] )
        # Step 2: Create a Set() to store visited vertices
        #         NOTE: Sets are a good data structure b/c: they're 
        #               unordered and don't have duplicated items
        visited = set()
        # Step 3: Use a WHILE loop that continues while queue is NOT empty
        while q.size() > 0:
            # Step 4a: Dequeue the FIRST PATH [to evaluate each of it's 
            #         vertices] and set it equal to a variable
            path = q.dequeue()
            # Step 4b: Grab the VERTEX from the end of the path [to evaluate]
            current_vert = path[-1]
            # Step 4c: If current_vert == destination_vertex_id, return path
            if current_vert == destination_vertex_id:
                return path
            if current_vert not in visited:
            # Step 5: If the current_vert has NOT been visited, add it into the 
            #         set() as an item
                visited.add(current_vert)
                # Step 6: Use a FOR loop that iterates over EACH of 
                #         current_vert's neighbors, creating a NEW 
                #         copy of the path for EACH neighbor, but each
                #         neighbor now becomes the NEW 'current_vert'
                #         for their OWN path, which is added to the
                #         end of the queue, to be evaluated later
                for neighbor in self.vertices[current_vert]:
                    # Step 7: Copy the path
                    path_copy = list(path)
                    # Step 8: Append the neighbor to the end of the copied path
                    path_copy.append(neighbor)
                    # Step 9: Enqueue the copied path
                    q.enqueue(path_copy)

    def dfs(self, starting_vertex_id, destination_vertex_id):
        # Step 1: Create an empty STACK and push the starting_vertex_id,
        #         WITHIN an array, to the end of the stack (b/c we're 
        #         storing PATHS this time, not "vertices")
        s = Stack()
        s.push( [starting_vertex_id] )
        # Step 2: Create a Set() to store visited vertices
        #         NOTE: Sets are a good data structure b/c: they're 
        #               unordered and don't have duplicated items
        visited = set()
        # Step 3: Use a WHILE loop that continues while the stack is NOT empty
        while s.size() > 0:
            # Step 4a: Pop the FIRST PATH [to evaluate each of it's 
            #         vertices] and set it equal to a variable
            path = s.pop()
            # Step 4b: Grab the VERTEX from the end of the path [to evaluate]
            current_vert = path[-1]
            # Step 4c: If current_vert == destination_vertex_id, return path
            if current_vert == destination_vertex_id:
                return path
            if current_vert not in visited:
            # Step 5: If the current_vert has NOT been visited, add it into the 
            #         set() as an item
                visited.add(current_vert)
                # Step 6: Use a FOR loop that iterates over EACH of 
                #         current_vert's neighbors, creating a NEW 
                #         copy of the path for EACH neighbor, but each
                #         neighbor NOW becomes the NEW 'current_vert'
                #         for their OWN path, which is added to the
                #         end of the queue, to be evaluated later
                for neighbor in self.vertices[current_vert]:
                    # Step 7: Copy the path
                    path_copy = list(path) # Creates a copy of the list
                    # Step 8: Append the neighbor to the end of the copied path
                    path_copy.append(neighbor)
                    # Step 9: Push the copied path
                    s.push(path_copy)





if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print("Vertices in Graph:\n")
    print(graph.vertices)
    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("\n\n---------------------------------------------------------------\n")
    print("DFT path:")
    graph.dft(1)
    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print("\n\n---------------------------------------------------------------\n")
    print("BFT path:")
    graph.bft(1)
    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("\n\n---------------------------------------------------------------\n")
    print("DFT-recursive path:")
    graph.dft_recursive(1)
    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("\n\n---------------------------------------------------------------\n")
    print("BFS path with shortest # nodes:")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("\n\n---------------------------------------------------------------\n")
    print("DFS path in depth first order:")
    print(graph.dfs(1, 6))
