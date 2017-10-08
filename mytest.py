#------ Problem: Dollar to RMB --------------

# Ask the user to input $ and assign it tp the $ variable
dollar = input("Press dollars:")
# Convert from string to integer
dollar = int(dollar)
# Perform calculation by multiplying 6.74 times $
CNY = dollar * 6.75
# Print result using format()
print("{} dollars equals {} Yuan".format(dollar,CNY))