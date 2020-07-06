from node import Node

class LinkedList:
  def __init__(self):
    self.head = None
    self.last = None
    self.length = 0

  def push(self, value):
    if (self.head is None):
      self.head = Node(value, None)
      self.last = self.head
    else:
      temp = Node(value, None)
      self.last.next = temp
      self.last = temp

    # Increase length by 1
    self.length += 1


