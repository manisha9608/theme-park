from linked_list import LinkedList

class HashTable:
  def __init__(self, size):
    self.__size = size
    self.__array = [LinkedList()] * size

  def hash(self, key):
    return key % self.__size

  def add(self, key, value):
    # Add key, value in hash table
    index = self.hash(key)
    list = self.__array[index]
    list.push(value)


  def get(self, key):
    # return value corresponding to key
    index = self.hash(key)
    list = self.__array[index]
    return list.get(key)

  def length(self):
    #return length of table
    return self.__array.length
