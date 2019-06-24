class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

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

class Graph:
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")
          
def bft(self, starting_vertex_id):
    # Create an empty Queue and enqueue the starting_vertex_id
    q = Queue()
    q.enqueue(starting_vertex_id)
    # Create a Set to store visited vertices
    # Sets are a good choice b/c: unordered and items in sets are NOT repeated
    visited = set()
    # While the queue is NOT empty:
    while q.size() > 0:
        # Dequeue the first vertex
        v = q.dequeue()
        # If that vertex has not been visited:
        if v not in visited:
            # Mark it as visited
            print(v)
            visited.add(v)
            # Add all of it's neighbors to the back of the queue
            for next_vert in self.vertices[v]:
                q.enqueue(next_vert)        
                    
def dft(self, starting_vertex_id):
    # Create an empty Stack and push the starting_vertex_id
    s = Stack()
    s.push(starting_vertex_id)
    # Create a Set to store visited vertices
    # Sets are a good choice b/c: unordered and items in sets are NOT repeated
    visited = set()
    # While the stack is NOT empty:
    while s.size() > 0:
        # Pop the first vertex (which equals the last one added)
        v = s.pop()
        # If that vertex has not been visited:
        if v not in visited:
            # Mark it as visited
            print(v)
            visited.add(v)
            # Add all of it's neighbors to the back of the queue
            for next_vert in self.vertices[v]:
                s.push(next_vert)    
            
def bfs(self, starting_vertex_id, target_vertex_id):
    # Create an empty queue and enqueue A PATH TO the starting vertex ID
    # Create a Set to store visited vertices
    # While the queue is not empty...
        # Dequeue the first PATH
        # Grab the last vertex from the PATH
        # If that vertex has not been visited...
            # CHECK IF IT'S THE TARGET
              # IF SO, RETURN PATH
            # Mark it as visited...
            # Then add A PATH TO its neighbors to the back of the queue
              # COPY THE PATH
              # APPEND THE NEIGHOR TO THE BACK
    pass