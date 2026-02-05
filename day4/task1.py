contact={"farwez":123456,
         "sahad":789012,
         "siddiq":5634276}
print(contact)
contact["movi"]=635337
print(contact.get("farwez"))
print(contact.get("zidane","contact not found"))
for key,values in contact.items():
    print("contact:",key,"phone",values)
