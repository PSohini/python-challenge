# import the os module
import os
#Module for reading csv files
import csv
#Files to load 
file_to_load = os.path.join('election_data.csv')
print(file_to_load)
#Declare Global Variables

with open(file_to_load, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    reader = csv.reader(file_to_load, delimiter=',')
  
#Get Total Votes.Count Rows
row_count = sum(1 for line in open(file_to_load))

#Generate Output Summary
output = (
          f"\n Election Results \n"
          f"---------------------------------\n"
          f"Total Votes: {row_count}\n"
          f"---------------------------------\n")
          #f"Average Change : ${net_monthly_avg:.2f}\n"
          #f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
          #f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
print(output)

#Write output file
# Set variable for output file
output_file = os.path.join("pypoll_final.csv")

# Display results on output file
with open(output_file, "w") as txt_file:
   txt_file.write(output)
