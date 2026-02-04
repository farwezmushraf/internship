'''
str1 = "farwez"
str2 = "mushraf"
combained_str= str1 + " "+str2
print(combained_str)

message = " hello world! "
print(message.strip())
print(message.upper())
print(message.replace("world","python"))
'
text="python programming"
print(text[0:6])
print(text[:6])
print(text[7:])
print(text[:-1])
print(text[::-3])
print(text[-3:])
print(text[3::])


text2="python is highly + interpreted language"
print(text2.split())
b= text2.split()
print(b)
for word in b:
    print(word)

print("i love \"python programming\"\"farwez\"")


a=[1,2,3,4,5,6]
a.append(7)
a.sort(reverse=True)
a.remove(6)
a.extend([8,9])
a.pop(4)
a.count(3)
print(a)


tuple1=(100,200,300,400,500,600,700)
print(tuple1)
tuple1.count(200)
print(tuple1.count(200))
print(tuple1.index(300))


add={1,2,3,4,5,6}
add.add(7)
add.remove(4)
print(add)

set={"name":"farwez","age":22,"palce":"banglore"}
print(set)
print(set["age"])
set["age"]=25
set["professsion"]="developer"
print(set)

sum=lambda a,b:a+b
print(sum(2,5))


values=[1,2,3,4,5,6]
print(list(map(lambda x:x+3,values)))

print(list(filter(lambda x:x%2==0,values)))

from functools import reduce
product=reduce(lambda x,y:x+y,values)
print(product)

'''


