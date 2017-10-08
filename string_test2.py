## --------------------string methods --------------
#from string import join
rand_string = '   life is A beautiful struggle   '
print (rand_string)

#delete space on the left
rand_string1= rand_string.lstrip()
print (rand_string1)

#delete space on the right
rand_string2= rand_string.rstrip()
print (rand_string2)

#delete spaces on the right and left
rand_string3= rand_string.strip()
print (rand_string3)

print (rand_string)
print ()

# capitalize first letter
print (rand_string.capitalize())

#capitalize every letter
print (rand_string.upper())

#lowercase all letter
print (rand_string.lower())
print ("")


test_list = ['yangle','is','a','good','man']

print(''.join(test_list))
print ('*'.join(test_list))

print("")

test_list2=rand_string.split()
print (test_list2)

print (rand_string)
print ("how many 'if' :",rand_string.count("if"))
print ("where is 'is' :",rand_string.find("is"))

print (rand_string.replace("struggle","journey"))