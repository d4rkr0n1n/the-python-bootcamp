# Conditional statements

# if statement
x = 10
if x > 5:
    print("x is greater than 5")

# if-else statement
if x < 5:
    print("x is less than 5")
else:
    print("x is greater than 5")

# if-elif-else statement
if x < 5:
    print("x is less than 5")
elif x == 5:
    print("x is equal to 5")
else:
    
    print("x is greater than 5")

# Nested if statement
if x > 5:
    if x == 10:
        print("x is equal to 10")
    else:
        print("x is greater than 5 but not equal to 10")

# Short Hand If
if x > 5: print("x is greater than 5")

# Short Hand If-Else
print("x is greater than 5") if x > 5 else print("x is less than 5")

# Multiple conditions in a single line
if x > 5 and x < 15: print("x is greater than 5 and less than 15")

# if-else with 3 conditions
print("x is greater than 5") if x > 5 else print("x is equal to 5") if x == 5 else print("x is less than 5")
