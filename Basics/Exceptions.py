# Exceptions

# try-except block
try:
  x = int("6.9")
except:
  print("Exception occurred")

# try-except block (specific error)
try:
  x = int("6.9")
except ValueError:
  print("Exception occurred (ValueError)")

# else block if no error
try:
  x = int("6.9")
except ValueError:
  print("Exception occurred (ValueError)")
else:
  print("No exception occurred")


# finally block (always executed)
try:
  x = int("6.9")
except ValueError:
  print("Exception occurred (ValueError)")
finally:
  print("Finally block executed")

# raise an exception
try:
  x = -1
  if x < 0:
    raise Exception("x is not a whole number")
except Exception as e:
  print("An exception occurred with details:",e)

# raise a specific exception
try:
  x = -1
  if not type(x) is str:
    raise TypeError("x is not a string")
except TypeError as e:
  print("An exception occurred with details: ",e)