#------ if test -----

#name=raw_input('Enter User ID:')
#name = 'yangle'

#if name == 'yangle':
#    print("hello ,my dad")
#
#else:
#    print('go away,')


# ---------------- user loading (if...elif & while)----------------------
# can input times
input_times=5

while input_times >=1:
    name = raw_input("what's your name?'")

    pass_wd = raw_input("press password:")
    if name == 'yangle' and pass_wd == 'yl1234':
        print("welcome!")
        break

    elif name != 'yangle' and pass_wd == 'yl1234':
        print('name or password not current')
        input_times=input_times-1
        remaining_times = str(input_times)
        print('you still have ' + remaining_times + ' times to input')
        if input_times == 0:
            print('you are not allow enter')
            break

    elif name =='yangle' and pass_wd !='yl1234':
        print('name or password not current')
        input_times = input_times - 1
        remaining_times = str(input_times)
        print('you still have '+ remaining_times + ' times to input')
        if input_times == 0:
            print('you are not allow enter')
            break

    else:
        # print("fuck off!")
        print('your password not current')
        input_times = input_times - 1
        remaining_times=str(input_times)
        print('you still have ' + remaining_times + ' times to input')
        if input_times == 0:
            print('your input times is over,you are not allow enter')


#-------------------