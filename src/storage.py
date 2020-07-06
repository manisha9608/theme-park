from hashtable import HashTable

class Storage:
  def __init__(self):
    # self.__city_table = HashTable(11)
    # self.__user_table = HashTable(101)

    self.__storage_table = HashTable(101)

    self.__birthday_table = HashTable(365)

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
      city_table.add(visitorObject.getCity(), (city_count if city_count is not None else 0) + 1)
      user_table.add(visitorObject.getFirstName(), visitorObject)

    # insert in birthday table
    self.__birthday_table.add(visitorObject.getDateOfBirth(), visitorObject)

  def find_visitor(self, date_of_visit, first_name):
    return first_name

  def get_visitor_count(self, date_of_visit):
    return date_of_visit

  def get_tending_city(self, date_of_visit):
    return date_of_visit

  def get_birthday_people(self, dob1, dob2):
    return dob2
