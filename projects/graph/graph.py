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
        if vertex_1_id in self.vertices and vertex_2_id in self.vertices:
            self.vertices[vertex_1_id].add(vertex_2_id)
        else:
            raise IndexError("That vertex does not exist")
    def bft(self, starting_vertex_id):
        # Step 1: Create an empty QUEUE and enqueue the starting_vertex_id
        q = Queue()
        q.enqueue(starting_vertex_id)
        # Step 2: Create a Set() to store visited vertices
        #         NOTE: Sets are a good data structure b/c: they're 
        #               unordered and no duplicated items
        visited = set()
        # Step 3: Use a WHILE loop that continues while queue is NOT empty
        while q.size() > 0:
            # Step 4: Dequeue the FIRST vertex [to evaluate] and set equal
            #         to a variable
            current_vert = q.dequeue()
            if current_vert not in visited:
                # Step 5: If it has NOT been visited, add it into the set 
                #         as an item
                print()
                visited.add(current_vert)
                # Step 6: Use a FOR loop that iterates over each of current_vert's
                #         neighbors, adding each one to end of the queue
                for next_vert in self.vertices[current_vert]:
                    q.enqueue(next_vert)
        
    def dft(self, starting_vertex_id):
        """
        Print each vertex_id in depth-first order
        beginning from starting_vertex_id.
        """
        pass  # TODO
    def dft_recursive(self, starting_vertex_id):
        """
        Print each vertex_id in depth-first order
        beginning from starting_vertex_id.
        This should be done using recursion.
        """
        pass  # TODO
    def bfs(self, starting_vertex_id, destination_vertex_id):
        """
        Return a list containing the shortest path from
        starting_vertex_id to destination_vertex_id in
        breath-first order.
        """
        pass  # TODO
    def dfs(self, starting_vertex_id, destination_vertex_id):
        """
        Return a list containing a path from
        starting_vertex_id to destination_vertex_id in
        depth-first order.
        """
        pass  # TODO





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
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
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
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
