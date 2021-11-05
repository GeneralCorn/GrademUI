#!/usr/bin/env python3
from csv import reader

fs = list()

with open('./sentences.csv', 'r') as read_obj:

    csv_reader = reader(read_obj)
    
    for i in range(7):
        fs.append(list())

    for col in csv_reader:
        for i in range(7):
            fs[i].append(col[0])

print(fs) # fs = list_of_rows
