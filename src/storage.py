from hashtable import HashTable
from birthday_table import BirthdayTable
from datetime import datetime, timedelta

class Storage:
  def __init__(self):

    self.__storage_table = HashTable(11)

    self.__birthday_table = BirthdayTable(366)

  def insert(self, visitorObject):
    date_of_visit = visitorObject.getDateOfVisit()
    arr = self.__storage_table.get(date_of_visit)
    if (arr is None):
      # record doesn't exist
      city_table = HashTable(11)
      user_table = HashTable(101)

      city_table.add(visitorObject.getCity(), 1)
      user_table.add(visitorObject.getFirstName(), visitorObject)
      self.__storage_table.add(date_of_visit, [city_table, user_table])
    else:
      # record corresponding to date_of_visit exists
      # add visitor object
      city_table = arr[0]
      user_table = arr[1]

      city_count = city_table.get(visitorObject.getCity())
      if (city_count is None):
        # city doesn't exist
        city_table.add(visitorObject.getCity(), 1)
      else:
        # record already present for city
        city_table.update(visitorObject.getCity(), city_count + 1)

      user_table.add(visitorObject.getFirstName(), visitorObject)

    # insert in birthday table
    birthday_key = datetime.strptime(visitorObject.getDateOfBirth().strftime('%d-%b'), '%d-%b')
    self.__birthday_table.add(birthday_key, visitorObject)

    # print table content
    # print('Printing table contents')
    # print('Storage table:')
    # self.__storage_table.print()

    # print('Prinnting birthday table:\n\n')
    # self.__birthday_table.print()

  def find_visitor(self, date_of_visit, first_name):
    arr = self.__storage_table.get(date_of_visit)
    if (arr is None):
      return []

    user_table = arr[1]

    return user_table.getAll(first_name)


  def get_visitor_count(self, date_of_visit):
    arr = self.__storage_table.get(date_of_visit)
    if (arr is None):
      return None

    user_table = arr[1]
    return user_table.length()

  def get_tending_city(self, date_of_visit):
    arr = self.__storage_table.get(date_of_visit)
    if (arr is None):
      return None

    city_table = arr[0]

    max = -1
    city = ''
    for obj in city_table:
      if (obj is not None):
        key = obj[0]
        value = obj[1]
        if (value > max):
          max = value
          city = key

    return (city, max)

  def get_birthday_visitors(self, dob1, dob2):
    if (dob1 > dob2):
      return []
    date = dob1
    visitors = []
    while date <= dob2:
      visitors += self.__birthday_table.getAll(date)
      date += timedelta(days=1)
    return visitors
