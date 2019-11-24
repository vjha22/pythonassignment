class EmailErr(Exception):
    def __init__(self,msg="error in Email!"):
        Exception.__init__(self,msg)
        
class PassErr(Exception):
    def __init__(self,msg="error in Password!"):
        Exception.__init__(self,msg)
            
try:
    names={"Dhoni":"icc","Saurav":"bcci","Rahul":"sdfr"}
    name=input("Enter name: ")
    password=input("Enter password: ")
    for i in names
    if i not in names.keys():
        raise EmailErr

        if password not in names.values():
            raise PassErr
      
    else:
        print("Welcome "+ name)

except EmailErr as e:
    print(e)
except PassErr as e:
    print(e)
  
print("Some other task")