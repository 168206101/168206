
'''四个犯人编号1，2，3，4，
a说：thief != 1

b说：thief  = 4

c说：thief  = 2

d说：thief != 4'''

for i in range(4):
    i += 1
    if 1 == ((i != 1) + (i == 4) + (i == 2) + (i != 4)):
        str = chr(96 + i) + "是小偷！"
        print(str)
