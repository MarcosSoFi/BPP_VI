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


#   [2] Results
#	----------------------------------------------------------------
expenses_m 	= []
savings_m   = []

for i in second_check[1]:
	expenses = []
	expenses_m.append(expenses)
	savings	 = []
	savings_m.append(savings)
	for j in i:
		if j > 0:
			savings.append(j)
		else:
			expenses.append(j)

expenses_m_t = [sum(i) for i in expenses_m]
savings_m_t  = [sum(i) for i in savings_m]


# 	2.1 Highest Expending/Saving Month
#	----------------------------------------------------------------
expending_Month = months[expenses_m_t.index(max(expenses_m_t))]
saving_Month    = months[savings_m_t.index(max(savings_m_t))]

print("Highest Expending Month - ", expending_Month)
print("Highest Saving Month    - ", saving_Month)


# 	2.2 Monthly Means
#	----------------------------------------------------------------
expenses_mean = sum(expenses_m_t) / len(months)
savings_mean  = sum(savings_m_t) / len(months)

print("Expenses Mean = ", round(expenses_mean,2),"€")
print("Savings Mean  = ", round(savings_mean,2),"€")


# 	2.3 Totals
#	----------------------------------------------------------------
expenses_year = sum(expenses_m_t)
savings_year  = sum(savings_m_t)

print("Total Expenses = ", expenses_year,"€")
print("Total Savings  = ", savings_year,"€")



