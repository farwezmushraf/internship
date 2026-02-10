name = input("enter your name is ")
goal = input("enter your goal is")

file=open("journal.txt","a")
file.write(f"name {name}\tgoal{goal}\n" )
file.close

