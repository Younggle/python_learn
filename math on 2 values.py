# -------------Math on 2 values ------------

#input 5 4
# 5 + 4 = 9
# 5 - 4 = 1
# 5 * 4 = 20
# 5 / 4 = 1.25
# 5 % 4 = 1

# ask the user to inout 2 values and store them in varable

truth=1
while truth>0:
# split() splits inout using whitespace
# num1,num2 = raw_input("Enter 2 number:").split()
    num1,operator,num2 = raw_input("Enter what you want operate:").split()
#convert the values entered and store in sum
    num1 = float(num1)
    num2 = float(num2)

    if operator == '+':
        print('{} + {} = {}').format(num1,num2,num1 + num2)
#add the values entered and store in sum
#    sum = num1 + num2
    elif operator =="-":
        print("{} - {} = {}").format(num1,num2,num1 - num2)
# subsract the values entered and store in difference
# difference = num1 - num2
    elif operator == "*":
        print("{} * {} = {}").format(num1,num2,num1 * num2)

# Mulitiply the values entered and store in product
# product = num1 * num2
    elif operator == "/":
        print("{} / {} = {}").format(num1,num2,num1 / num2)
#Divide values entered and store in quotient
#quotient = num1 / num2
    elif operator == "%":
        print ("{} % {} = {}").format(num1,num2,num1 % num2)
#use modulus on values entered and store in remainder
#remainder = num1 % num2

    else:
        print("sorry, I only supports '+','-','*','/','%'")
# Print the results
# format() loads the variable values in order into the
# {} placeholders

#print("{} + {} = {}".format(num1,num2,sum))
#print("{} - {} = {}".format(num1,num2,difference))
#print("{} * {} = {}".format(num1,num2,product))
#print("{} / {} = {}".format(num1,num2,quotient))
#print("{} % {} = {}".format(num1,num2,remainder))