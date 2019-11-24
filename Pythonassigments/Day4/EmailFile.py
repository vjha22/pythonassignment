import os
import re
print(os.chdir("C:\\Users\\vjha22\\Desktop\\Assignments\\Day4\\test"))
print(os.getcwd())
for file in os.listdir("C:\\Users\\vjha22\\Desktop\\Assignments\\Day4\\test"):
    if file.endswith('.log'):
        fo=open(file,'r')
        for line in fo:
            s=re.findall('[^@]+@[^@]+\.[^@]+', line)
            if(len(s)!=0):
                print(s)



   

