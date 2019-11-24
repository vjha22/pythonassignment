ob = [{'pId':'1','pName':'earphones', 'cost':'1000','brand':'boats','rating':'3',"discount":'10',"category":"electronics"},
      {'pId':'2','pName':'mobile','cost':'1500','brand':'one plus','rating':'2',"discount":'200',"category":"electronics"},
      {'pId':'3','pName':'fridge','cost':'17000','brand':'LG','rating':'4',"discount":'35',"category":"electronics"},
      {'pId':'4','pName':'tv','cost':'64000','brand':'samsung','rating':'5',"discount":'45',"category":"electronis"}
      
    ] 
  
def sorting(i):
        switcher={
                0:'cost',
                1:'rating',
                2:'discount',
                
            }
       
        sortCategory=switcher.get(i)
        sortType = int(input("Enter 1 if sort in ascending order"))
        if(sortType==1):
            ob.sort(key=lambda el: el[sortCategory])
            print(ob)

        else:
            ob.sort(key=lambda el: el[sortCategory],reverse=True)

            print(ob)
categor=int(input("Enter category: 0:cost, 1:rating, 2:discount"))
sorting(categor)

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

brandName=input("Enter brand name")
newobj = filter(lambda el:el["brand"]==brandName,ob)
for i in newobj:
    print('{pName} {brand}'.format(**i))
    
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
prodName=input("Enter product name")
newobj = filter(lambda el:el["pName"]==prodName,ob)
for i in newobj:
    print('{pName} {brand}'.format(**i))