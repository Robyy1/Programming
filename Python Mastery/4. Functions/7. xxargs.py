
def save_user(**user):
    print(user)
    
save_user(id=1, name="John", age=22)




def save_user(**user):
    print(user["id"])
    print(user["name"])
    print(user["age"])
    
save_user(id=1, name="John", age=22)
