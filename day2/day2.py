
age=21
height=5.8
name="farwez"
is_stundent=True

print(type(age))
print(type(height))
print(type(name))
print(type(is_stundent))

name=input("enter your name:")
age=input("enter your age:")
age=int(age)

new_age= age + 4
print( "Hey " + name + " You will be " + str(new_age) + " In 2030 ") 


print("Bill_splitter")
total_bill=float(input("Enter total bill amount"))
num_people=int(input("enter the number of people to split bill"))
per_person=total_bill/num_people

print("Total bill " + str(total_bill) + " Each person pays " + str(per_person))

print("profil_card")
item_name="laptop"
quant=2
price=499.99
in_stock= True
print(" item: " + item_name + ", quantity " + str(quant) + ", price " + str(price) + ", in stock " + str(in_stock))
total_cost= quant*price
print(" total cost " + str(total_cost))



