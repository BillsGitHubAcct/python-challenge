def cmp(a, b):  # compare list a and list b and return 0 if they are equal
    return (a > b) - (a < b)


def ssn_hide_5_char(string_var):
    i = 0
    new_string = ""
    for char in string_var:
        if char != "-" and i <= 5:
            char = "*"
        i += 1
        new_string += char
    return (new_string)


def reformat_date(date_str):
    if len(date_str[-2:]) == 1:
        date_str[-2] = '0' + date_str[-2:]
    if len(date_str[5:7]) == 1:
        date_str[5:7] = '0' + date_str[5:7]
    return(date_str[-2:] + "/" + date_str[5:7] +  "/" + date_str[0:4])

import os
import csv
import operator
import us_states_abbrev


csv_path = os.path.join('Resources', 'employee_data1.csv')
out_path = os.path.join('Resources', 'fmtted_emp_data1.csv')

saveRow = []
# ------------------------------------
# Create new file having unique rows 
# ------------------------------------
with open(csv_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')  # Read csv
    out = csv.writer(open(out_path, "w", newline=''), delimiter=',', quoting=csv.QUOTE_ALL)
    row_count = 0
    for row in csvreader:
        if row_count > 0:
            ssn_value = row[3]
            row[3] = ssn_hide_5_char(ssn_value)
            date = row[2]
            row[2] = reformat_date(date)
            row[4] = us_state_abbrev[row[4]]
            
        out.writerow(row)
        row_count +=1

dupCount = 0
partialDupCount = 0
# --------------------------------------------
# Lookup title in unique row file 
# ---------------------------------------------
# saveRow = []
# firstRow = True
# titleFound = False
# with open(out_path,newline='') as uniquecsvfile:
# 	uniquecsvreader = csv.reader(uniquecsvfile, delimiter=',') # Read unique csv
# 	outreader = csv.reader(uniquecsvfile, delimiter=',') # Read csv
# 	titleRequest = input("What show do you want to look up? ")
# 	for row in outreader:
# 		if titleRequest == row[0]:
# 			titleFound = True
# 			if firstRow:
# 				printLine = row[0] + " is rated " + row[1] + " with a rating of " + row[3]
# 				saveRow = row
# 				firstRow = False
# 			else:
# 				if cmp(row,saveRow) == 0:
# 					dupCount += 1  # This can't happen now since dups are removed
# 				else:
# 					partialDupCount +=1
#
# 		else:
# 			if titleFound:
# 				print(printLine + " (full dups: -->" + str(dupCount)  + " partial dups: -->" + str(partialDupCount) + ")")
# 				break
#
# 	if not titleFound:
# 		print(titleRequest + " was Not Found")
