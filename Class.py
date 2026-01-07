class UserProfile:
  def __init__(self, username , age):
    self.username = username
    self.age = age
  
  @property
  def username(self):
    return self._username
  @property
  def age(self):
    return self._age
  @username.setter
  def username(self, name):
    if len(name) < 3:
      print("Invalid username")
    else:
      self._username = name
  @age.setter
  def age(self , value):
    if value < 0 or value > 120:
      print("Invalid age")
    else:
      self._age = value
jarvis = UserProfile("itsjarvisonly",21)
print(jarvis.username)
print(jarvis.age)
jarvis.age = 55
print(jarvis.age)





  # @username.setter
  # if len(username) < 3:
  #   print("")