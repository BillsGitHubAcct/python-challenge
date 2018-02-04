
def ssn_hide_5_char(string_var):
    """ Function returns SSN with first 5 number blanked out  """
    i = 0
    new_string = ""
    for char in string_var:
        if char != "-" and i <= 5:
            char = "*"
        i += 1
        new_string += char
    return (new_string)


def reformat_date(date_str):
    """ Function reformats date from yyyy-mm-dd to dd/mm/yyyy """
    if len(date_str[-2:]) == 1:
        date_str[-2] = '0' + date_str[-2:]
    if len(date_str[5:7]) == 1:
        date_str[5:7] = '0' + date_str[5:7]
    return(date_str[-2:] + "/" + date_str[5:7] +  "/" + date_str[0:4])

import os
import csv
import us_states_abbrev
import pandas as pd
import numpy as np
#
#   PYBoss program 1. prompts the user for the number of data files to process
#                  2. formats the data files to fmtted data files until the next data file doesn't exist
#                     and/or the number of files to process has been reached
#
new_row = []
print("----------------------------------------------------------------------")
file_number = int(input("Enter number of employee data files to reformat -->"))
print("----------------------------------------------------------------------")
file_count = 1
csv_path = os.path.join('Resources', 'employee_data' + str(file_count) + '.csv')
out_path = os.path.join('Resources', 'fmtted_emp_data' + str(file_count) + '.csv')
# While data files exist and count less or equal the user specified number of data files
while os.path.exists(csv_path) and file_count <= file_number:
    # ------------------------------------
    # Create new csv file(s) having new and reformatted rows
    # ------------------------------------
    with open(csv_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')  # Read csv
        ofile = open(out_path, "w", newline='')
        out = csv.writer(ofile, delimiter=',')
        header_row = True
        for row in csvreader:
            if not header_row:
                # reformat detail row and write it to formatted file
                new_row.append(row[0])
                names = row[1].split( )
                new_row.append(names[0])
                new_row.append(names[1])
                date = row[2]
                new_row.append(reformat_date(date))
                ssn_value = row[3]
                new_row.append(ssn_hide_5_char(ssn_value))
                new_row.append(us_states_abbrev.us_state_abbrev[row[4]])
                out.writerow(new_row)
                new_row = []
            else:
                # insert new column headers and write header to formatted file
                new_row.append(row[0])
                new_row.append("First Name")
                new_row.append("Last Name")
                new_row.append(row[2])
                new_row.append(row[3])
                new_row.append(row[4])
                out.writerow(new_row)
                new_row = []
                header_row = False

    print("---> Data file processed: " + csv_path)
    print("---> Formatted file created: " + out_path)
    print("--------------------------------------------")
    file_count += 1
    row_counter = 0
    csv_path = os.path.join('Resources', 'employee_data' + str(file_count) + '.csv')
    out_path = os.path.join('Resources', 'fmtted_emp_data' + str(file_count) + '.csv')
