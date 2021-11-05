#!/usr/bin/env python3

with open('sentences.csv', 'r+') as csv:
    data = csv.readlines()

fs = list()

for line in data:
    fs.append(line.split("|"))

# Outputs a 2D array, where the fs[score][commentIndex]
# 3rd comment in score of 7
print(fs[6][2])
