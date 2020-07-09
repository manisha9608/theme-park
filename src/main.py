from visitor import Visitor
from storage import Storage

class Main:
  def __init__(self):
    self.__parkStorage = Storage()
    self.__today = ''
    self.__output = open('outputPS2.txt','w')

  def insertVisitor(self):
    f = open('src/inputPS2.txt', 'r')
    lines = f.readlines()
    for line in lines:
      info = line.strip().split(',')
      name = info[0].split(' ')
      visitorObj = Visitor(name[0].strip(), name[1].strip(), info[1].strip(),
        info[2].strip(), info[3].strip(), info[4].strip())
      self.__parkStorage.insert(visitorObj)
      print(line)

  def findVisitor(self, first_name):
    date_of_visit = self.__today
    visitors = self.__parkStorage.find_visitor(date_of_visit, first_name)
    # print('{} visitors with name ‘{}’ found visiting on {}'.format(visitors.length, first_name, date_of_visit))
    self.__output.writelines(["\n---------- findVisitor: ---------- \n",str(visitors.length)," visitors with name ",first_name," on ", date_of_visit,"\n"])
    for visitor in visitors:
      # print('{} {}, {}, {}'.format(visitor.getFirstName(), visitor.getLastName(), visitor.getCity(), visitor.getPhoneNumber()))
      self.__output.write(visitor.getFirstName() + " " + visitor.getLastName() + " " + visitor.getCity() + " " + visitor.getPhoneNumber() + "\n")
    self.__output.write("\n-----------------------------")

  def visitorCount(self, date_of_visit):
    count = self.__parkStorage.get_visitor_count(date_of_visit)
    # print('{} visitors found visiting on {}'.format(count, date_of_visit))
    self.__output.writelines(["\n---------- visitorCount: ---------- \n",str(count)," visitors found visiting on ",date_of_visit, "\n","-----------------------------"])

  def cityVisitor(self):
    (city, count) = self.__parkStorage.get_tending_city(self.__today)
    # print('{} visitors from {} visiting today'.format(count, city))
    self.__output.writelines(["\n---------- trendCity: ---------- \n",str(count)," visitors from ",city, "visiting today\n","-----------------------------"])


  def birthdayVisitor(self, birth_date_from, birth_date_to):
    visitors = self.__parkStorage.get_birthday_visitors(birth_date_from, birth_date_to)
    print('{} visitors have upcoming birthdays between {} and {}'.format(visitors.length, birth_date_from, birth_date_to))
    for visitor in visitors:
      print('{} {}, {}, {}'.format(visitor.getFirstName(), visitor.getLastName, visitor.getDateOfBirth(), visitor.getPhoneNumber))

park = Main()
park.insertVisitor()
