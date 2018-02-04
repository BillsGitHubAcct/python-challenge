import os
import pandas as pd
import csv
CONVERT_MONTH = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06",
                 "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
continue_proc = "y"
continue_processing = {"y": True, "yes": True, "n": False, "no": False}
asterisk_list = []
asterisk = ""
# Main loop
while continue_processing[continue_proc]:
    file_list = []
    index_list = []
    print("------------------------------------------------")
    # Display files in resources to select from
    for index, file in enumerate(os.listdir('Resources')):
        file_list.append(file)
        index_list.append(index)
        asterisk_list.append(asterisk)
        print(str(index + 1) + " " + file + asterisk_list[index])
    if "*" in asterisk_list:
        print("*processed")
    print("------------------------------------------------")
    # Prompt for file number
    file_select = int(input("Please enter the # of budget file to process -->"))
    while file_select - 1 not in index_list:
        file_select = int(input('  "' + str(file_select) + '" is not valid.... try again -->'))
    # Initialize paths to files based on file selection
    wrk_path = os.path.join("work_data.csv")
    csv_path = os.path.join("Resources", file_list[file_select - 1])
    rpt_list_string = str(file_list[file_select - 1])[:-4]
    rpt_txt_file = rpt_list_string + "_report.txt"
    rpt_path = os.path.join("Save-Reports", rpt_txt_file)
    print("\nYou chose: " + file_list[file_select - 1])
    asterisk_list[file_select - 1] = "*"
    new_row = []
    header = 1
    # Read from budget csv and to work csv file including new columns for sorting on later
    with open(csv_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        with open(wrk_path, "w", newline='') as outfile:
            csvwriter = csv.writer(outfile, delimiter=',')
            for row in csvreader:
                if not header:
                    # Write non-header row to work file
                    date_parts = str(row[0]).split("-")  # from "Date" value split to get month and year
                    new_row.append(int(date_parts[1]))  # insert new column for "Year"
                    new_row.append(CONVERT_MONTH[date_parts[0]])  # insert new column for numeric month value
                    new_row.append(row[0])
                    new_row.append(row[1])
                    csvwriter.writerow(new_row)
                    new_row = []
                else:
                    # Write header row to work file
                    new_row.append("Year")
                    new_row.append("NumMth")
                    new_row.append(row[0])
                    new_row.append(row[1])
                    csvwriter.writerow(new_row)
                    new_row = []
                    header = 0
    # Now read work file in pandas fpr doing the data analysis
    df = pd.read_csv(wrk_path)
    list_months = df["Date"].unique()
    unique_months = len(list_months)
    total = df["Revenue"].sum()
    count_days = df["Date"].count()
    avg_rev_change = total/unique_months
    #  Instantiate a sorted Dataframe on month number and date columns
    sorted_df=df.sort_values(["Year", "NumMth"])
    # Following code gets max revenue increase and max revenue decrease between days
    prev_revenue = 0
    max_rev_increase = 0
    max_rev_increase_date = ""
    max_rev_decrease = 0
    max_rev_decrease_date = ""
    revenue_change  = 0

    # Loop through sorted Dataframe and accumulate max values
    first_row = True
    for index, row in sorted_df.iterrows():
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
    fina_report = "\n\n-------------------------------\n"       \
                + 'Total Months: ' + str(unique_months) +"\n"   \
                + "Total Revenue: ${:0,.0f}".format(total) +"\n"   \
                + "Average Revenue Change: ${:0,.0f}".format(avg_rev_change) +"\n" \
                + "Greatest Increase in Revenue: {} (${:0,.0f})".format(max_rev_increase_date,max_rev_increase) +"\n" \
                + "Greatest Decrease in Revenue: {} (${:0,.0f})".format(max_rev_decrease_date,max_rev_decrease)
    # wrote it to screen
    print(fina_report)
    # write it to text file
    with open(rpt_path, "wt") as out_file:
        out_file.write(fina_report)
    print("\nSummary written to: " + rpt_path)
    # prompt to continue
    continue_proc = input("\nChoose Another File? y/n -->").lower()
    while continue_proc not in continue_processing:
        continue_proc = input('  "' + str(continue_proc) + '" is not valid.... try again -->').lower()
