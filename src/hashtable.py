from linked_list import LinkedList

class HashTable:
  def __init__(self, size):
    self.__tableSize = size
    self.__array = [LinkedList() for i in range(size)]
    self.__size = size
    self.__length = 0

  def hash(self, key):
    return hash(key) % self.__tableSize

  def add(self, key, value):
    # Add key, value in hash table
    # Time Complexity = O(1)
    index = self.hash(key)
    list = self.__array[index]
    list.insertAtHead(key,value)
    self.__length+=1


  def get(self, key):
    # return value corresponding to key
    index = self.hash(key)
    list = self.__array[index]
    return list.get(key)

  def getAll(self, key):
    # return all values corresponding to key
    index = self.hash(key)
    list = self.__array[index]
    return list.getAll(key)

  def __setitem__(self, key, value):
        self.add(key, value)

  def __getitem__(self, key):
      return self.get(key)

  def length(self):
    #return length of table
    return self.__length

  def print(self):
    for index,list in enumerate(self.__array):
      print('hash key: ', index)
      list.print()

  def __iter__(self):
    self.__i = 0
    self.__l = 0

    return self

  def __next__(self):
    if (self.__i < self.__size):
      list = self.__array[self.__i]
      if (self.__l >= list.length):
        self.__i +=1
        self.__l = 0
        self.__next__()
      else:
        self.__l += 1
        return list.getByIndex(self.__l-1)
      return self.__i
    else:
      raise StopIteration
