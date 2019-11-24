class ValidationErr(Exception):
    def __init__(self,msg="error in credentials!"):
        Exception.__init__(self,msg)
            
try:
    names={"Dhoni":"icc","Saurav":"bcci","Rahul":"sdfr"}
    name=input("Enter name: ")
    password=input("Enter password: ")
    if name not in names.keys():
        raise ValidationErr
    elif password not in names.values():
        raise ValidationErr
    else:
        print("Welcome "+ name)

except ValidationErr as e:
    print(e)
  
print("Some other task")