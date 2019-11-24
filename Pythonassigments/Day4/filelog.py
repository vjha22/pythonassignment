import os
cdir=os.listdir("C:\\Users\\vjha22\\Desktop\\Assignments\\DAy4\\multiple\\levels")


for i in cdir:

    li=os.path.splitext(i)
    if li[1] == '.log':
        print(i)



