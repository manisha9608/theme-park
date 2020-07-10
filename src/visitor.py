from datetime import datetime

class Visitor:

  def __init__(self, firstName, lastName, dov, dob, city, phoneNumber):
    self.setFirstName(firstName)
    self.setLastName(lastName)
    self.setDateOfVisit(dov)
    self.setDateOfBirth(dob)
    self.setCity(city)
    self.setPhoneNumber(phoneNumber)

  def getFirstName(self):
    return self.__firstName

  def setFirstName(self, firstName):
    self.__firstName = str(firstName.strip())

  def getLastName(self):
    return self.__lastName

  def setLastName(self, lastName):
    self.__lastName = str(lastName.strip())

  def getName(self):
    return self.__firstName + self.__lastName

  def getDateOfVisit(self):
    return self.__dov

  def setDateOfVisit(self, dov):
    try:
      date_of_visit = datetime.strptime(dov.strip(), '%d-%b-%Y')
      self.__dov = date_of_visit
    except:
      raise ValueError('Unexpected date of visit')

  def getDateOfBirth(self):
    return self.__dob

  def setDateOfBirth(self, dob):
    try:
      date_of_birth = datetime.strptime(dob.strip(), '%d-%b-%Y')
      self.__dob = date_of_birth
    except:
      raise ValueError('Unexpected date of birth')

  def getCity(self):
    return self.__city

  def setCity(self, city):
    self.__city = str(city.strip())

  def getPhoneNumber(self):
    return self.__phoneNumber

  def setPhoneNumber(self, phoneNumber):
    self.__phoneNumber = str(phoneNumber.strip())
