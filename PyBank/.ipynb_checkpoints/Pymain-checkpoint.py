{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import libraries\n",
    "import os, csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [],
   "source": [
    "#variables for the script\n",
    "months = []        #list of months\n",
    "pl =[]             #list of monthly PL\n",
    "pl_changes = []    #list of P&L Changes\n",
    "n_months = 0       #count of months\n",
    "pl_total = 0       #total of P&L\n",
    "plc = 0            #variable to track PL changes\n",
    "avg_pl_change = 0  #average of changes in PL\n",
    "maxpl = 0          #maximum increase in profits\n",
    "minpl = 0          #maximum decrease in losses\n",
    "max_i = 0          #index for max pl\n",
    "min_i = 0          #index for min pl\n",
    "\n",
    "#read the resource file\n",
    "bankcsv = os.path.join(\".\", \"Resources\", \"budget_data.csv\")    #set path\n",
    "\n",
    "\n",
    "#read file\n",
    "with open(bankcsv, 'r') as csv_file:\n",
    "    csv_reader = csv.reader(csv_file,delimiter=\",\")\n",
    "    header = next(csv_reader)\n",
    "    \n",
    "    #for loop to update the counters and lists\n",
    "    for row in csv_reader:\n",
    "        n_months += 1\n",
    "        pl_total += int(row[1])\n",
    "        pl.append(row[1])\n",
    "        months.append(row[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [],
   "source": [
    "# loop to track the PL change values\n",
    "pl_changes = [] \n",
    "plc = int(pl[0])\n",
    "for i in range(1, len(pl)):\n",
    "    pl_changes.append(int(pl[i]) - plc)\n",
    "    plc = int(pl[i])\n",
    "    i += 1\n",
    "#print(pl_changes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [],
   "source": [
    "#calculate the average PL Changes, max and min\n",
    "avg_pl_change = sum(pl_changes) / len(pl_changes)\n",
    "maxpl = max(pl_changes)\n",
    "minpl = min(pl_changes)\n",
    "#print(avg_pl_change, maxpl, minpl)\n",
    "#print(pl_changes.index(maxpl))\n",
    "#print(len(pl_changes))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "---------------------------------------------------------------------\n",
      "Total Months: 86\n",
      "Total: $38382578\n",
      "Average Change: $-2315.12\n",
      "Greatest Increase in Profits: Feb-2012  ($1926159)\n",
      "Greatest Decrease in Profits: Sep-2013 ($-2196167)\n"
     ]
    }
   ],
   "source": [
    "#find dates for max and min PL changes\n",
    "max_i = pl_changes.index(maxpl) +1    #adding +1 since the changes are calculated one row above\n",
    "min_i = pl_changes.index(minpl) +1\n",
    "\n",
    "maxmonth = months[max_i]\n",
    "minmonth = months[min_i]\n",
    "\n",
    "#print output to the terminal\n",
    "\n",
    "print(\"Financial Analysis\")\n",
    "print(\"-\"*69)\n",
    "print(f\"Total Months: {n_months}\")\n",
    "print(f\"Total: ${round(pl_total,2)}\")\n",
    "print(f\"Average Change: ${round(avg_pl_change,2)}\")\n",
    "print(f\"Greatest Increase in Profits: {maxmonth}  (${maxpl})\")\n",
    "print(f\"Greatest Decrease in Profits: {minmonth} (${minpl})\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [],
   "source": [
    "# write summary to txt file\n",
    "output = os.path.join(\".\",\"Analysis\", \"summary.txt\")\n",
    "\n",
    "# use \"\\n\" to create a new line\n",
    "with  open(output, 'w') as output:\n",
    "    output.write(\"Financial Analysis\\n\")\n",
    "    output.write(\"-\"*69 + \"\\n\")\n",
    "    output.write(f\"Total Months: {n_months}\\n\")\n",
    "    output.write(f\"Total: ${round(pl_total,2)}\\n\")\n",
    "    output.write(f\"Average Change: ${round(avg_pl_change,2)}\\n\")\n",
    "    output.write(f\"Greatest Increase in Profits: {maxmonth}  (${maxpl})\\n\")\n",
    "    output.write(f\"Greatest Decrease in Profits: {minmonth} (${minpl})\\n\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
