# Functions

def my_func():
  print("Hello from a function")

my_func()

def my_func2(name):
  print("Hello, " + name)

my_func2("John")

def my_func3(name = "John",age=25):
  print("Hello, " + name)
  print("Age: " + str(age))

my_func3("John", 30)

def my_func4(*kids):
  print("The youngest child is " + kids[2])

my_func4("Emil", "Tobias", "Linus")

def my_func5(child3, child2, child1):
  print("The youngest child is " + child3)

my_func5(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def my_func6(**kid):
  print("His last name is " + kid["lname"])

my_func6(fname = "Tobias", lname = "Refsnes")

def my_func7(country = "Norway"):
  print("I am from " + country)

my_func7("Sweden")

def my_func8(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]