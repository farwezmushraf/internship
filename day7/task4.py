name1=input("enter the name 1:")
marks1=int(input("enter the marks1:"))

name2=input("enter the name 2:")
marks2=int(input("enter the marks2:"))

name3=input("enter the name 3:")
marks3=int(input("enter the marks3:"))

with open("names.txt","a") as file1:
    file1.write(f"{name1}\n{name2}\n{name3}\n")
    
with open("marks.txt","a") as file3:
    file3.write(f"{name1} - {marks1}\n")
    file3.write(f"{name2} - {marks2}\n")
    file3.write(f"{name3} - {marks3}\n")

    