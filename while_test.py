from __future__ import print_function
# --------- WHILE TEST ------------

# i = 0
# while i <5:
#     i +=1
#     if i == 3:
#         continue
#     print("i = ",i)

## ---------- christmas tree --------------------

tree_height = raw_input("input tree's height:")

tree_height = int(tree_height)

spaces = tree_height - 1

hashes = 1

stump_space=tree_height -1

while  tree_height != 0:

    for i in range(spaces):
        print(' ', end='')

    for i in range(hashes):
        print('%',end = '')

    print()

    hashes += 2

    tree_height -= 1

    spaces -= 1

for i in range(stump_space):
    print(" " ,end ='')

print ("8")