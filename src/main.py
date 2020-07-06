from visitor import Visitor
from storage import Storage

class Main:
  def __init__(self):
    self.__parkStorage = Storage()

  def insertvisitor(self):
    f = open('src/inputPS2.txt', 'r')
    lines = f.readlines()
    for line in lines:
      info = line.strip().split(',')
      name = info[0].split(' ')
      visitorObj = Visitor(name[0].strip(), name[1].strip(), info[1].strip(),
        info[2].strip(), info[3].strip(), info[4].strip())
      self.__parkStorage.insert(visitorObj)
      print(line)

park = Main()
park.insertvisitor()
