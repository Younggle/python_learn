# ---------------- split() test----------------
str = ("www.baidu.com/tu pian/gao xiao/index.html")
print str

# split by space
str_split1 = str.split()
print('split by space: {}') .format(str_split1)

# split all str by /
str_split2 = str.split('/')
print('split by "/": {}') .format(str_split2)

# only split 2 times by /
str_split3 = str.split('/',2)
print('split by "/": {}') .format(str_split3)

print('------------------------------------')
# can not < 4 but can > 4
str_split_1,str_split_2,str_split_3,str_split_4 = str.split('/',5)
print('split by "/":{}').format(str_split_1)
print('split by "/":{}').format(str_split_2)
print('split by "/":{}').format(str_split_3)
print('split by "/":{}').format(str_split_4)