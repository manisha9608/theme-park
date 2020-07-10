from visitor import Visitor
from storage import Storage
from datetime import datetime

def date_to_string(date):
  return date.strftime('%d-%b-%Y')

class App:
  def __init__(self):
    self.__parkStorage = Storage()
    self.__today = None
    self.__output = open('outputPS2.txt','w')

  def __del__(self):
    self.__output.close()

  def insertVisitor(self):
    f = open('src/inputPS2.txt', 'r')
    lines = f.readlines()
    count = 0
    for line in lines:
      try:
        info = line.strip().split(',')
        name = info[0].split(' ', 1) # split by first occurrence oly
        first_name = name[0].strip()
        last_name = ''
        if (len(name) == 2):
          last_name = name[1].strip()
        visitorObj = Visitor(first_name, last_name, info[1].strip(),
          info[2].strip(), info[3].strip(), info[4].strip())
        date_of_visit = visitorObj.getDateOfVisit()

        if (self.__today is None or self.__today < date_of_visit):
          self.__today = date_of_visit
        self.__parkStorage.insert(visitorObj)
        count += 1

      except Exception as error:
        print('error occurred while insertig visitor', error)

    self.__output.writelines(["\n---------- insert ----------\nTotal visitors detailed entered: ",
      str(count), "\n-----------------------------"])
    f.close()

  def findVisitor(self, first_name):
    date_of_visit = self.__today
    visitors = self.__parkStorage.find_visitor(date_of_visit, first_name)
    # print('{} visitors with name ‘{}’ found visiting on {}'.format(visitors.length, first_name, date_of_visit))
    self.__output.writelines(["\n---------- findVisitor: ---------- \n",
      str(len(visitors))," visitors with name ", first_name, " on ", date_to_string(date_of_visit), "\n"])
    for visitor in visitors:
      # print('{} {}, {}, {}'.format(visitor.getFirstName(), visitor.getLastName(), visitor.getCity(), visitor.getPhoneNumber()))
      self.__output.write(visitor.getFirstName()+ " "+ visitor.getLastName()+ " "+
        visitor.getCity()+ " "+ visitor.getPhoneNumber()+ "\n")
    self.__output.write("\n-----------------------------")

  def visitorCount(self, date_of_visit):
    date_time = datetime.strptime(date_of_visit.strip(), '%d-%b-%Y')
    count = self.__parkStorage.get_visitor_count(date_time)
    # print('{} visitors found visiting on {}'.format(count, date_of_visit))
    self.__output.writelines(["\n---------- visitorCount: ---------- \n",str(count),
      " visitors found visiting on ",date_of_visit, "\n","-----------------------------"])

  def cityVisitor(self):
    (city, count) = self.__parkStorage.get_tending_city(self.__today)
    # print('{} visitors from {} visiting today'.format(count, city))
    self.__output.writelines(["\n---------- trendCity: ---------- \n",
      str(count)," visitors from ",city, "visiting today\n","-----------------------------"])


  def birthdayVisitor(self, birth_date_from, birth_date_to):
    dob_from = datetime.strptime(birth_date_from.strip(), '%d-%b')
    dob_to = datetime.strptime(birth_date_to.strip(), '%d-%b')
    visitors = self.__parkStorage.get_birthday_visitors(dob_from, dob_to)
    self.__output.writelines(["\n---------- birthdayVisitor: ---------- \n",
      str(len(visitors)), " visitors have upcoming birthdays between ", birth_date_from, " and ", birth_date_to, "\n"])
    for visitor in visitors:
      #print('{} {}, {}, {}'.format(visitor.getFirstName(), visitor.getLastName, visitor.getDateOfBirth(), visitor.getPhoneNumber))
      self.__output.write(visitor.getFirstName()+ " "+ visitor.getLastName()+ " "+
        date_to_string(visitor.getDateOfBirth())+ " "+ visitor.getPhoneNumber()+ "\n")

    self.__output.write("-----------------------------")

def main():
  park = App()
  park.insertVisitor()
  prompt = open('src/promptsPS2.txt','r')
  lines = prompt.readlines()
  for line in lines:
        input = line.strip('\n').strip().split(':')
        tag = input[0].strip()
        if (tag == 'findVisitor'):
          park.findVisitor(input[1].strip())
        elif (tag == 'visitorCount'):
          park.visitorCount(input[1].strip())
        elif (tag == 'trendCity'):
          park.cityVisitor()
        elif (tag == 'birthdayVisitor'):
          park.birthdayVisitor(input[1].strip(), input[2].strip())
        else:
          print('No valid input')

  prompt.close()

main()