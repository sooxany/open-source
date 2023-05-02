# decorator

# 교수님 말씀 : way1 과  way2의 차이를 알아야함 
# Way 1
# A Python program to demonstrate that a function
# can be defined inside another function and a
# function can be passed as parameter.
# Adds a welcome message to the string
def messageWithWelcome(str):
 # Nested function
 def addWelcome():
    return "Welcome to "
 # Return concatenation of addWelcome()
 # and str.
 return addWelcome() + str
# To get site name to which welcome is added
def site(site_name):
 return site_name
print(messageWithWelcome(site("Computer Science World!")))



# Way 2
# Adds a welcome message to the string
# returned by fun(). Takes fun() as
# parameter and returns welcome().
def decorate_message(fun):
 # Nested function
 def addWelcome(site_name):
  return "Welcome to " + fun(site_name)
 # Decorator returns a function
 return addWelcome
@decorate_message # Use a decorator
def site(site_name):
 return site_name;
# This call is equivalent to call to
# decorate_message() with function
# site("Computer Science World!") as parameter
print(site("Computer Science World!"))


