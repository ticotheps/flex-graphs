import random
import math
import time

class Queue:
	def __init__(self):
		self.queue = []
	def enqueue(self, value):
		self.queue.append(value)
	def dequeue(self):
		if (self.size) != 0:
			return self.queue.pop(0)
		else:
			return None
	def size(self):
		return len(self.queue)

class User:
	def __init__(self, name):
		self.name = name

class SocialGraph:
	def __init__(self):
		self.lastID = 0
		self.users = {}
		self.friendships = {}

	def addFriendship(self, userID, friendID):
		if userID == friendID:
			pass
		elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
			pass
		else:
			self.friendships[userID].add(friendID)
			self.friendships[friendID].add(userID)
			return True

	def addUser(self, name):
		self.lastID += 1
		self.users[self.lastID] = User(name)
		self.friendships[self.lastID] = set()

	def populateGraph(self, numUsers, avgFriendships):
		self.lastID = 0
		self.users = {}
		self.friendships = {}

		for i in range(numUsers):
			self.addUser(f"User {i + 1}")

		possibleFriendships = []
		for userID in self.users:
			for friendID in range(userID + 1, self.lastID + 1):
				possibleFriendships.append((userID, friendID))
		random.shuffle(possibleFriendships)
		for i in range(0, (numUsers * avgFriendships // 2)):
			friendship = possibleFriendships[i]
			self.addFriendship(friendship[0], friendship[1])

	def populateGraphLinear(self, numUsers, avgFriendships):
		self.lastID = 0
		self.users = {}
		self.friendships = {}

		for i in range(numUsers):
			self.addUser(f"User {i + 1}")
		
		targetFriendships = (numUsers * avgFriendships) // 2
		totalFriendships = 0
		collisions = 0

		while totalFriendships < targetFriendships:
			userID = random.randint(1, self.lastID)
			friendID = random.randint(1, self.lastID)
			if self.addFriendship(userID, friendID):
				totalFriendships += 2
			else:
				collisions += 1
		print(f"COLLISIONS: {collisions}")

	def getAllSocialPaths(self, userID):
		visited = {}
		q = Queue()
		q.enqueue([userID])
		while q.size() != 0:
			path = q.dequeue()
			newUserID = path[-1]
			if newUserID not in visited:
				visited[newUserID] = path
				for friendID in self.friendships[newUserID]:
					if friendID not in visited:
						new_path = list(path)
						new_path.append(friendID)
						q.enqueue(new_path)
		return visited

if __name__ == '__main__':
	sg = SocialGraph()
	totalConnections = 0
	totalDegrees = 0
	iterations = 10

	for i in range(0, iterations):
		sg.populateGraph(1000, 5)
		connections = sg.getAllSocialPaths(1)
		total = 0
		for userID in connections:
			total += len(connections[userID]) - 1

		totalConnections += len(connections)
		totalDegrees += total / len(connections)

		print("------------")
		print(f"Friends in network: {len(connections)}")
		print(f"Average degrees: {total / len(connections)}")

	print(f"Average Connections: {totalConnections / iterations}")
	print(f"Average Degrees: {totalDegrees / iterations}")

if __name__ == '__main__':
	sg = SocialGraph()
	numUsers = 50000
	avgFriendships = 100
	linear_start_time = time.time()
	sg.populateGraphLinear(numUsers, avgFriendships)
	linear_end_time = time.time()
	print(f"Linear runtime: {linear_end_time - linear_start_time}")
	quad_start_time = time.time()
	sg.populateGraph(numUsers, avgFriendships)
	quad_end_time = time.time()
	print(f"Quadratic runtime: {quad_end_time - quad_start_time}")