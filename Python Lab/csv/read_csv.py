import csv

file = open('list.csv', 'r', encoding='utf-8')

rdr = csv.reader(file)
for line in rdr:
    print(line)

file.close
