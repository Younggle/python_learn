# -*-coding:utf-8-*-

# chinese convert test
# 一个汉字在utf-8中占3个字节

Chinese_string = raw_input(u"请输入要加密的中文：")
char_code =''

print(Chinese_string)

print(len(Chinese_string))

for i in range(0,len(Chinese_string)-2,3):

    #char_code += ord(Chinese_string)
    #print (char_code)
    one_chinese = "u'"+str(Chinese_string[i]+Chinese_string[i+1]+Chinese_string[i+2])+"'"
    char_code = int(ord(one_chinese))
    print(Chinese_string[i]+Chinese_string[i+1]+Chinese_string[i+2])
    print(char_code)