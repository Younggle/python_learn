# -*-coding:utf-8-*-

# Receive the message to encrypt and the number of character to shift
message = raw_input("Enter your message:")
key = raw_input("How many character should we shift(-26 ~ 26):")


# Prepare your secret message
secret_message = ""

# Cycle through each character in the message
for char in message:

    # if it is a letter
    if char.isalpha():

        # Get unicode and add the shift amount
        char_code = ord(char) + int(key)

        # if uppercase
        if char.isupper():

            # if greater than "Z"
            if char_code > ord('Z'):
                char_code -= 26
            # if less than "a"
            if char_code < ord("a"):
                char_code += 26
        # if lowercase
        if char.islower():

            # if greater than "z"
            if char_code > ord("z"):
                char_code -= 26
            # if less than "A"
            if char_code < ord("A"):
                char_code += 26


        # Convert from code to letter and add to message
        secret_message += chr(char_code)

        # if not a letter leave the character as is

    else:
        secret_message += char

# print the encrypted message
print("encrypted message: ",secret_message)



#decryt the secret message
de_key = -int(key)

orig_message = ""

# Cycle through each character in the message
for char in secret_message:

    # if it is a letter
    if char.isalpha():

        # Get unicode and add the shift amount
        char_code = ord(char) + de_key

        # if uppercase
        if char.isupper():

            # if greater than "Z"
            if char_code > ord('Z'):
                char_code -= 26
            # if less than "A"
            if char_code < ord("A"):
                char_code += 26
        # if lowercase
        if char.islower():

            # if greater than "z"
            if char_code > ord("z"):
                char_code -= 26
            # if less than "a"
            if char_code < ord("a"):
                char_code += 26


        # Convert from code to letter and add to message
        orig_message += chr(char_code)

        # if not a letter leave the character as is

    else:
        orig_message += char

# print the encrypted message
print("original message: ",orig_message)

# 好气哦
