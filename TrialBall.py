position= []
name= []
count= int(input())
for i in range(0,count):
    ele= int(input())
    position.append(ele)
print(position)
for i in range(0,count):
    ele= input()
    name.append(ele)
n= len(position)
for i in range(0,n):
    if(position[i]== len(name[i])):
       name[i]= str.upper(name[i])
    else:
            name[i]= str.lower(name[i])
for i in range(n):
    for j in range(0, n-i-1):
        if position[j]>position[j+1]:
            name[j], name[j+1]= name[j+1],name[j]
            position[j], position[j+1]= position[j+1],position[j]
for i in range(0,n):
    print(name[i])
    