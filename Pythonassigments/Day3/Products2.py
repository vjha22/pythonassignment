
import operator
class product(object):
    def __init__(self,name,cost,brand,category,discount):
        self.name=name
        self.cost=cost
        self.brand=brand
        self.category=category
        self.discount=discount

    def showAll():
        print("Details Are\n")
        for i in productList:
            print({"name": str(i.name),"cost": str(i.cost),"brand":str(i.brand) ,"category":str(i.category),"discount":str(i.discount)})


productList=[]
productList.append(product("fridge","20000","electronics","Accessories","30%"))
productList.append(product("tv","50000","electronics","Fiction","30%"))
productList.append(product("Perfume","800","Titan","Grooming","20%"))

print("1.Sort by Cost low to high\n"
      "2.Sort by Cost high to low\n"
      "3.Sort by discount low to high\n"
      "4.Sort by discount high to low\n"
      "5.Filter by Brandname\n"
      "6.Filter by ProductName\n"
      
      )
choice=int(input("Enter your choice"))

if choice==1:
    productList.sort(key=operator.attrgetter('cost'))
    product.showAll()
elif choice==2:
    productList.sort(key=operator.attrgetter('cost'),reverse=True)
    product.showAll()
elif choice==3:
    productList.sort(key=operator.attrgetter('discount'))
    product.showAll()
elif choice==4:
    productList.sort(key=operator.attrgetter('discount'),reverse=True)
    product.showAll()
elif choice==5:
    brandName=input("Enter brand name")
    newobj = filter(lambda el:el.brand==brandName,productList)
    for i in newobj:
        print(i.name)
elif choice==6:
    productName=input("Enter product name")
    newobj = filter(lambda el:el.name==productName,productList)
    for i in newobj:
        print(i.cost,i.brand)

 

