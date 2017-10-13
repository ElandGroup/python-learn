fruits ={}

#add
fruits['test']='111'
fruits['color']='red'
fruits['color2']='yellow'
fruits['price']=10
print(fruits)


#update
fruits['color']='yellow'
print(fruits)

#delete

del fruits['test']
print(fruits)

print("1====")

for key,value in fruits.items():
    print(key)
    print(value)
print("2====")

for key in fruits.keys():
    print(key)
print("3====")

for value in fruits.values():
    print(value)
print("4====")


for key in sorted(fruits.keys()):
    print(key)
print("5====")

for value in set(fruits.values()):
    print(value)




