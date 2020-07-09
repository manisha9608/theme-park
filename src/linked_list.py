from node import Node

class LinkedList:
  def __init__(self):
    self.head = None
    self.length = 0

  def insertAtHead(self, key, value):
    # Time Complexity = O(1)
    temp = Node(key, value, self.head)
    self.head = temp

    # Increase length by 1
    self.length += 1

  def get(self, key):
    # returns first occurrence
    if (self.head is None):
      return None

    temp= self.head.clone()
    while(temp != None and temp.key != key):
      temp = temp.next

    if (temp is None):
      return None

    return temp.value

  def getAll(self, key):
    # returns all occurrence
    arr = []
    if (self.head is None):
      return None

    temp= self.head.clone()
    while(temp != None):
      if (temp.key == key):
        arr.append(temp.value)
      temp = temp.next

    return arr

  def getByIndex(self, index):
    if (index >= self.length):
      return None
    count = 0
    temp = self.head.clone()
    while(temp != None and count < index):
      temp = temp.next
    if (temp is None):
      return None
    if (count == index):
      return (temp.key, temp.value)

  def print(self):
    if (self.head is None):
      print('List is empty')
      return

    temp= self.head.clone()
    while(temp != None):
      print('list element: key: {} value: {} '.format(temp.key, temp.value))
      temp = temp.next




