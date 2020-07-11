from hashtable import HashTable
from birthday_table import BirthdayTable
from datetime import datetime, timedelta

class Storage:
  def __init__(self):
    # initialize storage and birthday table
    self.__storage_table = HashTable(101)

    self.__birthday_table = BirthdayTable(366)

  def insert(self, visitorObject):
    date_of_visit = visitorObject.getDateOfVisit()
    arr = self.__storage_table.get(date_of_visit)
    if (arr is None):
      # record doesn't exist
      # initialize city and user table
      city_table = HashTable(11)
      user_table = HashTable(101)

      city_table.add(visitorObject.getCity(), 1) # initialize count by 1
      user_table.add(visitorObject.getFirstName(), visitorObject)
      self.__storage_table.add(date_of_visit, [city_table, user_table])
    else:
      # record corresponding to date_of_visit exists
      # add visitor object
      city_table = arr[0]
      user_table = arr[1]

      city_count = city_table.get(visitorObject.getCity())
      if (city_count is None):
        # city doesn't exist in table
        city_table.add(visitorObject.getCity(), 1)
      else:
        # record already present for city
        # add 1 to existing count and update the record
        city_table.update(visitorObject.getCity(), city_count + 1)

      user_table.add(visitorObject.getFirstName(), visitorObject)

    # Ignore year from date_of_birth
    birthday_key = datetime.strptime(visitorObject.getDateOfBirth().strftime('%d-%b'), '%d-%b')
    # insert in birthday table
    self.__birthday_table.add(birthday_key, visitorObject)


  def find_visitor(self, date_of_visit, first_name):
    arr = self.__storage_table.get(date_of_visit)
    if (arr is None):
      # No visitor found on particular date_of_visit
      return []

    user_table = arr[1]

    return user_table.getAll(first_name) # get all visitors visted on date_of_visit


  def get_visitor_count(self, date_of_visit):
    arr = self.__storage_table.get(date_of_visit)
    if (arr is None):
      # No visitor found on particular date_of_visit
      return 0

    user_table = arr[1]
    return user_table.length() # return the count of visitors visited on date_of_visit

  def get_tending_city(self, date_of_visit):
    arr = self.__storage_table.get(date_of_visit)
    if (arr is None):
      # No visitor found on particular date_of_visit
      return ('', 0)

    city_table = arr[0]

    max = 0
    city = ''
    for obj in city_table:
      if (obj is not None):
        key = obj[0] # city
        value = obj[1] # visitor count
        if (value > max):
          max = value
          city = key

    return (city, max)

  def get_birthday_visitors(self, dob1, dob2):
    # Assumption: dob1 <= dob2
    if (dob1 > dob2):
      return []
    date = dob1
    visitors = []
    while date <= dob2:
      visitors += self.__birthday_table.getAll(date)
      date += timedelta(days=1) # Increase day by 1
    return visitors
