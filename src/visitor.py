class Visitor:

  def _init_(self, firstName, lastName, dov, dob, city, phoneNumber):
    self.__firstName = firstName
    self.__lastName = lastName
    self.__dov = dov
    self.__dob = dob
    self.__city = city
    self.__phoneNumber = phoneNumber

  def getFirstName(self):
    return self.__firstName

  def setFirstName(self, firstName):
    self.__firstName = firstName

  def getLastName(self):
    return self.__lastName

  def setLastName(self, lastName):
    self.__lastName = lastName

  def getName(self):
    return self.__firstName + self.__lastName

  def getDateOfVisit(self):
    return self.__dov

  def setDateOfVisit(self, dov):
    self.__dov = dov

  def getDateOfBirth(self):
    return self.__dob

  def setDateOfBirth(self, dob):
    self.__dob = dob

  def getCity(self):
    return self.__city

  def setCity(self, city):
    self.__city = city

  def getPhoneNumber(self):
    return self.__phoneNumber

  def setPhoneNumber(self, phoneNumber):
    self.__phoneNumber = phoneNumber
