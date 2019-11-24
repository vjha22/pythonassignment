num = int(input('Enter number'))

count=0
i=1
while (i<=num):
    if (num%i==0):
        print(i)
        count+=1
       
    i+=1
        
print(count)

