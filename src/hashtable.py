from linked_list import LinkedList

class HashTable:
  def __init__(self, size):
    self.__tableSize = size
    self.__array = [LinkedList() for i in range(size)]
    self.__size = 0

  def hash(self, key):
    return hash(key) % self.__tableSize

  def add(self, key, value):
    # Add key, value in hash table
    # Time Complexity = O(1)
    index = self.hash(key)
    list = self.__array[index]
    list.insertAtHead(key,value)
    self.__size+=1


  def get(self, key):
    # return value corresponding to key
    index = self.hash(key)
    list = self.__array[index]
    return list.get(key)

  def size(self):
    #return length of table
    return self.__size

  def print(self):
    for index,list in enumerate(self.__array):
      print('hash key: ', index)
      list.print()

