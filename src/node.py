class Node:
  def __init__(self, key = None, value = None, next_node = None):
    self.key = key
    self.value = value
    self.next = next_node

  def clone(self):
    return Node(self.key, self.value, self.next)

  def equals(self, other_node):
    if (isinstance(other_node, Node)
      and (type(self.value) == type(other_node.value))
      and (self.value == other_node.value)):
      return True

    return False