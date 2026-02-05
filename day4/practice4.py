'''
dict = {"name":"farwez","ag":23,"place":"banglore"}
print(dict)
dict["branch"]=["CSE","ISE","ECE"]
print("added new branch:",dict)
dict.pop("place")
print("modified dict:",dict)
dict["branch"].remove("ISE")
print("new dict:",dict)
print(list(dict.items())[2])
dict["devolper"]=["1","2","3"]
print("added devoper:",dict)

'''
set={"farwez","banglore","ise",23}
print(set)
set.remove("farwez")
print("remaining iteams: ",set)
set.discard(23)
print(set)

set1={1,2,3,4,5,6,7}
set2={2,3,4,5,6,7,8}
print("union:", set1.union(set2))
print("intersection:",set1.intersection(set2))
print("difference:",set1.difference(set2))

