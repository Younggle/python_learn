## -------------- for test-------------
#for i in [2,4,6,8]:
#   print("i =",i)
#

## -----range() -------

#print("My name is")
#for i in range(5):
#    print('My son' + str(i))

#i=range(0,10)
## i =[0,1,2,3,4,5,6,7,8,9]
#print('i=', i)

#for i in range(0,10,2):
#    print("i = "+ str(i))

#for i in range(6,0,-1):
#   print ("i = "+str(i))

# # empty sum variable
# total = 0
# for num in range(101):
#    total += num
#
# print('1+2+3+4+...+100 = '+str(total))

# use for loop through the list from 1 to 21
# for i in range(1,21):
#
#     if(i % 2) !=0:
#         print("i = "+str(i))


# --------------- COMPOUNDING INTEREST-----------------

# Each year : investment + investment * interest

# Ask for money investment and the interest
## can not use raw_input()!!!!!
money = input("How much to invest:")
interest_rate = input("Interest Rate: ")

# Convert value to a float round the percent
interest_rate = float(interest_rate) * 0.01

# after 10 year
for i in range(10):
    money = money + money * interest_rate

print("Investment after 10 years: {}").format(money)
