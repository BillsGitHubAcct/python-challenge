import os
import numpy as np
import pandas as pd
import csv
convert_month = {"Jan":"01","Feb":"02","Mar":"03","Apr":"04","May":"05","Jun":"06","Jul":"07","Aug":"08","Sep":"09","Oct":"10","Nov":"11","Dec":"12"}
#print(convert_month["Jan"])
wrk_path = os.path.join("Resources","work_data.csv")
csv_path = os.path.join("Resources","budget_data_1.csv")
rpt_path = os.path.join("Save-Reports","budget_data_1_report.txt")

new_row = []
row_count = 0
# The following code writes to a work file after converting date to a number
# and putting it in a column so it can be part of the sort later on
with open(csv_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    with open(wrk_path, "w",newline='') as outfile:
        csvwriter = csv.writer(outfile, delimiter=',')
        for row in csvreader:
            if row_count > 0:
                monthpt = str(row[0]).split("-")
                new_row.append(convert_month[monthpt[0]])
                new_row.append(row[0])
                new_row.append(row[1])
                csvwriter.writerow(new_row)
                new_row = []
            else:
                new_row.append("NumMth")
                new_row.append(row[0])
                new_row.append(row[1])
                csvwriter.writerow(new_row)
                new_row = []
            row_count +=1
# Mow read work file in pandas fpr doing the data analysis
df = pd.read_csv(wrk_path)
unique_months = df["NumMth"].unique()
print(unique_months)
print(len(unique_months))
total = df["Revenue"].sum()
print(total)
count_days = df["Date"].count()
print(count_days)
avg_rev_change = total/len(unique_months)
print(avg_rev_change)
#  Instantiate a sorted Dataframe on month number and date columns
sorted_df=df.sort_values(["NumMth","Date"])
print(sorted_df)

# Following code gets max revenue increase and max revenue decrease between days

prev_revenue = 0
max_rev_increase = 0
max_rev_increase_date = ""
max_rev_decrease = 0
max_rev_decrease_date = ""
revenue_change  = 0

# Loop through sorted Dataframe and accumulate max values
first_row = True
for index, row in sorted_df.iterrows() :
    if not first_row:
        revenue_change = row['Revenue'] - prev_revenue
        if revenue_change > max_rev_increase:
            max_rev_increase = revenue_change
            max_rev_increase_date = row['Date']
        if revenue_change < max_rev_decrease:
            max_rev_decrease = revenue_change
            max_rev_decrease_date = row['Date']
    else:
        first_row = False
    prev_revenue = row['Revenue']

#  Output totals to report
fina_report = "-------------------------------\n"              \
            + 'Total Months: ' + str(len(unique_months))+"\n"   \
             + "Total Revenue: ${:0,.0f}".format(total) +"\n"   \
            + "Average Revenue Change: ${:0,.0f}".format(avg_rev_change) +"\n" \
            + "Greatest Increase in Revenue: {} (${:0,.0f})".format(max_rev_increase_date,max_rev_increase) +"\n" \
            + "Greatest Decrease in Revenue: {} (${:0,.0f})".format(max_rev_decrease_date,max_rev_decrease)

print(fina_report)




