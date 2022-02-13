abc = "Some string"
print(abc)
print(abc * 2)
print(abc + abc)

['some string', 123 , "another string"]

list_var = ["some string", 123 , "another string"]
print(list_var)

list_var.append("other string")
print(list_var)

list_var.pop()
print(list_var) 

print(len(list_var))
print(len("an string"))

print(list_var[0])
print(list_var[1])
print(list_var[2])

#Another example

abc = [1, 2, 3]

print(abc[0])
print(abc[1])
print(abc[2])

#And another example

another_list = ["Justin", "John", "Matt"]
print(another_list)
matt_name = another_list[2]
print(matt_name)

#Don't question it....
the_list = [1,2,3]

the_list.pop(0)
print(the_list)
the_list.pop(0)
the_list.pop(0)
#the_list.pop(0)
the_list = [1,2,3]
the_list.pop(2)
#the_list.pop(2)
#the_list.pop(1000)
print(len(the_list))



#Dictionary

a_dict = {
    "abc": "A string",
    "another": "another string",
    "yetanother": "another string"}
print(a_dict)

a_dict["abc"] = "another new string"
print(a_dict)
a_dict

#Tuples

tup = ()
tup = ("abc", "abc")
print(tup)

tup = (
    ("another", "another"),
    ("more", "more"),
)
print(tup)
print(tup[0])
print(tup[0][0])

tup += ("yetanother", 123)
print(tup)
tup += (("yetanother", 123),)
print(tup)

the_list = []
abc = ["another", "another"]
the_list.append(abc)
print(the_list)