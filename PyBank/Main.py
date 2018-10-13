# import the os module
import os
#Module for reading csv files
import csv

#Files to load and output
file_to_load = os.path.join('..','PyBank','budget_data.csv')
file_to_output = os.path.join('..','Pybank','Budget_Analysis.txt')
# Method 2: Improved Reading using CSV module

with open(file_to_load, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

    print("let's do it again")

    for row in csvreader:
        print(row)


# Print all of the results (to terminal)
print(output)

# Save the results to analysis text file
#with open(file_to_output, "a") as txt_file:
 #   txt_file.write(output)
