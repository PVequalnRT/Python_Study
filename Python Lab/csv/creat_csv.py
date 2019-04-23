import csv

c_file = open('list.csv', 'w', encoding='utf-8', newline='')

wr = csv.writer(c_file)

wr.writerow([1,"미야코","3577"])
wr.writerow([2,"쥰","3353"])
wr.writerow([3,"리노","3574"])

c_file.close()
