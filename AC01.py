import csv
import matplotlib.pyplot as plt
import seaborn as sns


#   [1.1] Check 1 - Import file
#	----------------------------------------------------------------
file_name = "finanzas2020"

try:
	with open(f"{file_name}.csv", "r") as file:
		raw_data = [i for i in csv.reader(file)]
except IOError:
	print(f"File '{file_name}' not found")

data   = raw_data[1:] # Remove months names
months = [i.split("\t") for i in raw_data[0]][0] # Months


#   [1.2] Check 2 - 12 Columns / data in months
#	----------------------------------------------------------------
#	1.2.1 Remove "\t" from string
newdata = [[j.split("\t") for j in i][0] for i in data]

# 	1.2.2 Transpose matrix
t_data = list(map(list, zip(*newdata)))

#   1.2.3 Check 12 columns
assert len(t_data) == 12 ,"Number of columns ≠ 12"

#   1.2.4 Check data in all months
assert all([len(i) > 0 for i in t_data]) ,"No data found"


#   [1.3] Check 3 - Data
#	----------------------------------------------------------------
# 	1.3.1 Check data function
def checkdata(lst):
	errors = []
	lists  = []
	for i in lst:
		sublist = []
		lists.append(sublist)
		for j in i:
			try:
				sublist.append(int(j))
			except:
				if j.startswith("'") and j.endswith("'"):
					sublist.append(int(j[1:-1]))
				if isinstance(j, str):
					sublist.append(0)
				errors.append(j)
	return errors,lists

# 	1.3.2 See error types 
first_check = checkdata(t_data)			
print("Error Types", first_check[0])

# 	1.3.3 Removed errors
second_check = checkdata(first_check[1])
print("New Errors", second_check[0]), print("\n")




