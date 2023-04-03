def greet(name):
    print(f"Hi {name}")
    
print(greet("Mosh"))
    
    
    
def greet_1(name):
    print(f"Hi {name}")
    return "..."
    
print(greet_1("Mosh"))
    
    
    
def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Mosh")
file = open("content.txt", "w")
file.write(message)




