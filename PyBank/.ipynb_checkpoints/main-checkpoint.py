#!/usr/bin/env python
# coding: utf-8

# In[64]:


# Import libraries
import os, csv


# In[65]:


#variables for the script
months = []        #list of months
pl =[]             #list of monthly PL
pl_changes = []    #list of P&L Changes
n_months = 0       #count of months
pl_total = 0       #total of P&L
plc = 0            #variable to track PL changes
avg_pl_change = 0  #average of changes in PL
maxpl = 0          #maximum increase in profits
minpl = 0          #maximum decrease in losses
max_i = 0          #index for max pl
min_i = 0          #index for min pl


os.chdir(os.path.dirname(__file__))   #changes path to current py file
#read the resource file
bankcsv = os.path.join(".", "Resources", "budget_data.csv")    #set path


#read file
with open(bankcsv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")
    header = next(csv_reader)
    
    #for loop to update the counters and lists
    for row in csv_reader:
        n_months += 1
        pl_total += int(row[1])
        pl.append(row[1])
        months.append(row[0])


# In[66]:


# loop to track the PL change values
pl_changes = [] 
plc = int(pl[0])
for i in range(1, len(pl)):
    pl_changes.append(int(pl[i]) - plc)
    plc = int(pl[i])
    i += 1
#print(pl_changes)


# In[67]:


#calculate the average PL Changes, max and min
avg_pl_change = sum(pl_changes) / len(pl_changes)
maxpl = max(pl_changes)
minpl = min(pl_changes)
#print(avg_pl_change, maxpl, minpl)
#print(pl_changes.index(maxpl))
#print(len(pl_changes))


# In[68]:


#find dates for max and min PL changes
max_i = pl_changes.index(maxpl) +1    #adding +1 since the changes are calculated one row above
min_i = pl_changes.index(minpl) +1

maxmonth = months[max_i]
minmonth = months[min_i]

#print output to the terminal

print("Financial Analysis")
print("-"*69)
print(f"Total Months: {n_months}")
print(f"Total: ${round(pl_total,2)}")
print(f"Average Change: ${round(avg_pl_change,2)}")
print(f"Greatest Increase in Profits: {maxmonth}  (${maxpl})")
print(f"Greatest Decrease in Profits: {minmonth} (${minpl})")


# In[69]:


# write summary to txt file
output = os.path.join(".","Analysis", "summary.txt")

# use "\n" to create a new line
with  open(output, 'w') as output:
    output.write("Financial Analysis\n")
    output.write("-"*69 + "\n")
    output.write(f"Total Months: {n_months}\n")
    output.write(f"Total: ${round(pl_total,2)}\n")
    output.write(f"Average Change: ${round(avg_pl_change,2)}\n")
    output.write(f"Greatest Increase in Profits: {maxmonth}  (${maxpl})\n")
    output.write(f"Greatest Decrease in Profits: {minmonth} (${minpl})\n")

