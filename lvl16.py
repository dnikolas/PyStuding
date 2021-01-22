import csv

st = [['a', 2], ['b', 4]]
with open('1.csv', 'w') as f:
    xls = csv.writer(f)
    xls.writerows(st)
