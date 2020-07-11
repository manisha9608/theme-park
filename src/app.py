from visitor import Visitor
from storage import Storage
from datetime import datetime

def date_to_string(date):
  return date.strftime('%d-%b-%Y')

class App:
  def __init__(self, output_file):
    # Initialize storage class
    self.__parkStorage = Storage()
    self.__today = None
    self.__output = open(output_file,'w')

  def __del__(self):
    self.__output.close()

  def insertVisitor(self, input_file):
    f = open(input_file, 'r')
    lines = f.readlines()
    count = 0
    for line in lines:
      try:
        # process each line
        info = line.strip().split(',')
        name = info[0].split(' ', 1) # split by first occurrence only
        first_name = name[0].strip()
        last_name = ''
        if (len(name) == 2):
          # if user has first name only
          last_name = name[1].strip()
        visitorObj = Visitor(first_name, last_name, info[1].strip(),
          info[2].strip(), info[3].strip(), info[4].strip())
        date_of_visit = visitorObj.getDateOfVisit()

        if (self.__today is None or self.__today < date_of_visit):
          # today is the latest date
          self.__today = date_of_visit
        self.__parkStorage.insert(visitorObj)
        count += 1

      except Exception as error:
        print('error occurred while insertig visitor', error)

    self.__output.writelines(["\n---------- insert ----------\nTotal visitors detailed entered: ",
      str(count), "\n-----------------------------"])
    f.close()

  def findVisitor(self, first_name):
    try:
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

    except Exception as error:
      print('error occurred in findVisitor', error)

  def visitorCount(self, date_of_visit):
    try:
      date_time = datetime.strptime(date_of_visit.strip(), '%d-%b-%Y')
      count = self.__parkStorage.get_visitor_count(date_time)
      # print('{} visitors found visiting on {}'.format(count, date_of_visit))
      self.__output.writelines(["\n---------- visitorCount: ---------- \n",str(count),
        " visitors found visiting on ",date_of_visit, "\n","-----------------------------"])

    except Exception as error:
      print('error occurred in visitorCount', error)

  def cityVisitor(self):
    try:
      (city, count) = self.__parkStorage.get_tending_city(self.__today)
      # print('{} visitors from {} visiting today'.format(count, city))
      self.__output.writelines(["\n---------- trendCity: ---------- \n",
        str(count)," visitors from ",city, "visiting today\n","-----------------------------"])

    except Exception as error:
      print('error occurred in cityVisitor', error)


  def birthdayVisitor(self, birth_date_from, birth_date_to):
    try:
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

    except Exception as error:
      print('error occurred in birthdayVisitor', error)

def main():
  try:
    input = open('src/input.txt', 'r')
    files = input.readlines()
    if (len(files) <3):
      print('Please provide input, prompt and outpt files path')

    input_file = files[0].strip('\n').strip()
    prompt_file = files[1].strip('\n').strip()
    output_file = files[2].strip('\n').strip()
    park = App(output_file)
    park.insertVisitor(input_file)
    # open prompt file
    prompt = open(prompt_file,'r')
    lines = prompt.readlines()
    for line in lines:
          # process each line and identify tag
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

  except Exception as error:
    print('error occurred in main', error)

main()