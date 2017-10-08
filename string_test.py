#-*-coding:utf-8-*-
## -----------string_test ----------------

samp_string = 'whatever you are,but be a good one'

print (samp_string[0])

print (samp_string[-1])

print (samp_string[0:4])

print (samp_string[8:])

print (len(samp_string))

print ()

print (samp_string[::])

print (samp_string[::2])

print (samp_string[::-1])

print ('I love you'[::-1])
# 
print ()

print(samp_string)
for char in samp_string:
    print(char)

# cycle the code into characters 2 at a time
for i in range(0,len(samp_string)-1,2):
    print (samp_string[i] + samp_string[i+1])

print ("yl" + 'hello')

print ("okay" * 5)


# convert an int into a string
num_string = str(4)
print (num_string)

# Convert letter into unicode code
print ("A = ",ord("A"))

# Convert from unicode with char
print("66 = ",chr(66))

# 无法进行中文字符转换？
print(u'在',ord(u"在"))

print("22312 = ",unichr(22312))

# 可以执行中文转换了

print u"'烦啊'的unicode：",int(ord(u'烦')),int(ord(u'啊'))

print u'翻译',unichr(ord(u'烦')),unichr(ord(u'啊'))