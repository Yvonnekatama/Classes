class Student:#
   school="AkiraChix"
   def __init__(self,name,age):#CLASS INITIALIZER
      self.name=name
      self.age=age
 
   def speak(self):#CLASS METHOD
      return f"Hello my name is {self.name} I am {self.age} years old and I love {self.school}."
      