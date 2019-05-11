import csv

#f = open('c:\\folder\\file.csv','a')
#f.close()

with open('file.csv','r') as csv_file:
    f1 = csv.reader(csv_file, delimiter=',')
    for row in f1:
        print(row)