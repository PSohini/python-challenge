# import the os module
import os
#Module for reading csv files
import csv
TotalMonths = 0
Monthofchange=[]
Notchange=[]
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0


#Files to load and output
file_to_load = os.path.join('budget_data.csv')
print(file_to_load)
with open(file_to_load, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
# Set a variable to header and set that to next csv reader
    Header=next(csvreader)

    print(Header)

