# A variable created inside a function is available inside that function:

def myfunc():
  x = 300
  print(x)

myfunc()



















# # Bug
# def myfunc():
#   x = 300
#   print(x)

# myfunc()
# print(x)




# # A variable created outside of a function is global and can be used by anyone:

# x = 300

# def myfunc():
#   print(x)

# myfunc()

# print(x)