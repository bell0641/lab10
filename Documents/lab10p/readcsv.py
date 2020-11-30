import csv
name = input("enter the name of the file :")
with open (name, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for i in csv_reader :
        print(i)
