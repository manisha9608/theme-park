from hashtable import HashTable
from datetime import datetime

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

class BirthdayTable(HashTable):

  # override hash function for birthday table
  def hash(self, key):
    if (isinstance(key, datetime)):
      tuple = key.timetuple()
      day = 0
      if (tuple.tm_mday == 29 and tuple.tm_mon == 2):
        # 29th february, consider 366th day
        day = 366
      else:
        for i in range(tuple.tm_mon-1):
          day += month_days[i]
        day += tuple.tm_mday

      return day % self._tableSize
    else:
      return super().hash(key)