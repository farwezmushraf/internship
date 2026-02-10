import csv
with open("student.csv","r")as csv2:
   file =csv.reader(csv2)
   for row in file:
     if row[2] == "Pass":
      print("student who passed:",row[0])