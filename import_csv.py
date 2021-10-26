import csv
with open('ipl_league.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[1]=="city":
            continue
        elif((row[2] == "bat") and (row[8]==row[9])) :
            print(row)

print ("dharmesh"")