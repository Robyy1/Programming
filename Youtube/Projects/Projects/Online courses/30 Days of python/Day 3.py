#For loops

bag = [10 , 3213, 757623, 725, 123, 321, 563]
print(len(bag))

for item in bag:
    print(item)

i = 0
for item in bag:
    i += 1
    print(i)


for item in bag:
    if item == 10:
        print('yes!')



#While loops

i = 10
while i < 11:
    print("yup")
    i += 1

i = 0
while i < 1000:
    print(i)
    i += 1

#i = 0 
#while i < 10:
#    print("abc")