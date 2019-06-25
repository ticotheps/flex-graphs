# Example Problem

# Given two words (beginWord and endWord), and a dictionary’s word list, return the shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:

# Return None if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# Sample:
# beginWord = “hit”
# endWord = “cog”
# return: [‘hit’, ‘hot’, ‘cot’, ‘cog’]

# beginWord = “sail”
# endWord = “boat”
# [‘sail’, ‘bail’, ‘boil’, ‘boll’, ‘bolt’, ‘boat’]

# beginWord = “hungry”
# endWord = “happy”
# None 

f = open('words.txt', 'r')
words = f.read().split('\n')
f.close()

word_set = set()
for word in words:
    word_set.add(word.lower())

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
      
def get_neighbors(word):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    neighbors = []
    string_word = list(word)
    for i in range(len(string_word)):
        for letter in letters:
            temp_word = list(string_word)
            temp_word[i] = letter
            w = "".join(temp_word)
            if w != word and w in word_set:
                neighbors.append(w)
    return neighbors
      
def findLadders(begin_word, end_word):
    visited = set()
    q = Queue()
    q.enqueue([begin_word])
    while q.size > 0:
      path = q.dequeue()
      current_word = path[-1]
      if current_word not in visited:
          visited.add(current_word)
          if current_word == end_word:
              return path
      for neighbor in get_neighbors(current_word):
          path_copy = list(path)
          path_copy.append(neighbor)
          
print(findLadders("hit", "cog"))