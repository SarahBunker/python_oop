from classes_objects import Student

tim = Student()
print(tim.name)

# Person inherits from Student class
class Person(Student):
  pass

p1 = Person()
print(p1.name)