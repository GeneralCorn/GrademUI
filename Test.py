# +
from csv import reader

with open('./sentences.csv', 'r') as read_obj:

    csv_reader = reader(read_obj)
    
    fs7  = []
    fs6 = []

    for col in csv_reader:
        fs7.append(col[0])
        fs6.append(col[1])


    list_of_rows = []
    list_of_rows.append(fs7)
    list_of_rows.append(fs6)
    print(list_of_rows)
# -

from csv import reader
# read csv file as a list of lists
with open('./sentences.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)
    print(list_of_rows)




