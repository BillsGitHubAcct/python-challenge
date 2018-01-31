import os
import csv
import operator

def cmp(a,b):   # function compares list a and list b and returns 0 if equal
	return (a>b)-(a<b)
	


continueProcessing = {"y":True,"yes":True,"n":False,"no":False}
print(continueProcessing["y"])
contProcessing = "y"
totalMonths = 0
totalRevenue = 0.00
avgRevenueChg = 0.00
greatestIncrease = 0.00
greatestDecrease = 0.00

# mainLoop
count = 0
while (count < 9): 
	fileList = []
	print("------------------------------------------------")
	# Display files in resources to select from
	for index, file in enumerate(os.listdir('Resources')):
		print(index+1,file)
		fileList.append(file)
	print("------------------------------------------------")
	# Prompt for user's file number
	fileSelect = int(input("Please enter the # of dataset file to process -->"))
	print("------------------------------------------------")    
	csvpath = os.path.join('Resources',fileList[fileSelect-1])
	
	if os.path.exists(csvpath):
		with open(csvpath,newline='') as csvfile:
			csvreader = csv.reader(csvfile, delimiter=',')
			next(csvreader) #skip Header
			#sortedList = sorted(csvreader, key=operator.itemgetter(0), reverse=False) #Sort by Date 
			firstMth = True
			#for row in sortedList: # Read row from Sorted collection
			for row in csvreader:
				dtString = str(row[0])
				print("dtString is " + dtString)
				month = dtString[0:3]
				print("month is " + month)
								
	count = 10				
					
	
#Loop while continueProcessing = 'Y'
#Prompt user for which data set to process (found in Resources directory)
#Check if data set exists
#if data set exists then read and process data set
#if data set not found then send message saying data set not found 
#Prompt user to continue Y/N setting continueProcessing 
#End Loop
 
#
csvpath = os.path.join('Resources','budget_data_1')
#outpath = os.path.join('Resources','unique_netflix_ratings.csv')

saveRow = []
# ------------------------------------
# Create new file having unique rows 
# ------------------------------------
# if not(os.path.exists(outpath)): 
	# with open(csvpath,newline='') as csvfile:
		# csvreader = csv.reader(csvfile, delimiter=',') # Read csv
		# # Sort csv by title so we can skip duplicates based on Title
		# sortedList = sorted(csvreader, key=operator.itemgetter(0), reverse=False)
		# out = csv.writer(open(outpath,"w",newline=''), delimiter=',',quoting=csv.QUOTE_ALL)
		# for row in sortedList:
			# if cmp(row,saveRow) != 0:
				# out.writerow(row) #write unique row to excel 
			# saveRow = row
# dupCount = 0
# partialDupCount = 0
# # --------------------------------------------
# # Lookup title in unique row file 
# ----------------------------------------------
# saveRow = []
# firstRow = True
# titleFound = False 
# with open(outpath,newline='') as uniquecsvfile:
	# uniquecsvreader = csv.reader(uniquecsvfile, delimiter=',') # Read unique csv
	# outreader = csv.reader(uniquecsvfile, delimiter=',') # Read csv
	# titleRequest = input("What show do you want to look up? ")		
	# for row in outreader:
		# if titleRequest == row[0]:
			# titleFound = True
			# if firstRow:
				# printLine = row[0] + " is rated " + row[1] + " with a rating of " + row[3]
				# saveRow = row
				# firstRow = False
			# else:
				# if cmp(row,saveRow) == 0:
					# dupCount += 1  # This can't happen now since dups are removed 
				# else:
					# partialDupCount +=1
					
		# else:
			# if titleFound:
				# print(printLine + " (full dups: -->" + str(dupCount)  + " partial dups: -->" + str(partialDupCount) + ")")
				# break
				
	# if not titleFound:
		# print(titleRequest + " was Not Found")