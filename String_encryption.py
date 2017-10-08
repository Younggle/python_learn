## ---------------String encryption--------------
from __future__ import  print_function
# # Ask for a string
# str = raw_input("convert to acronym")
#
# # convert the string to all uppercase
# str = str.upper()
#
# # convert the string into a list
# listOfWords = str.split()
#
# #Cycle through the list
# for word in listOfWords:
#
#     # print the letter of the word
#     print(word[0],end = '')

# Input string to be encrypted
original_message = raw_input("input a uppercase:")
secret_message = ""
# cycle through each character in the string
for char in original_message:

# store each character code in secret message
    if char.isalpha():
        secret_message += str(ord(char) - 23)
    elif char.isspace():
        secret_message += str(ord(char))
# print "Secret message : 79"
print("Secert message: ",secret_message)

decryption_message = ""
# cycle through each character code 2 at a time

for i in range(0,len(secret_message)-1,2):
    char_code = secret_message[i] + secret_message[i+1]

    if char_code != "32":
        decryption_message += chr(int(char_code) + 23)
    else:
        decryption_message += chr(int(char_code))

print("decryption message: ",decryption_message)