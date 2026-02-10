import csv
with open("Company_Data (1).csv","r") as csv1:
    file = csv.reader(csv1)
    for row in file:
        print(row)