class MyClass:
  x = 5

p1 = MyClass()

print(p1.x)

'''
init function
- initializing different values in class
'''

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

# instantiating object from class

me = Person("Sarah", 30)

print(me.name)
print(me.age)

'''
delete property on object
'''
del me.age

# print(me.age) # AttributeError: 'Person' object has no attribute 'age'

'''
deleting object
'''
del me

# print(me) #NameError: name 'me' is not defined

'''
empty class
bypass error using pass
'''

class People:
  pass # no error

'''
Student class for inheritance
'''

class Student():
  name = "Tim"
  age = 34
  gender = "male"