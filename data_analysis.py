import csv
from settings import dataset_file


outfile = open(dataset_file, 'r', encoding='utf-8')
csv_file = csv.reader(outfile)
num = 0
for item in csv_file:
    if len(item) == 0 or item[0] == '':
        continue
    print(item)

