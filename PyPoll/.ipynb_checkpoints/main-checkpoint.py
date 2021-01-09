#!/usr/bin/env python
# coding: utf-8

# In[26]:


# Import libraries
import os, csv


# In[27]:


#read the resource file
os.chdir(os.path.dirname(__file__))     #set path to current directory for code
pollcsv = os.path.join(".", "Resources", "election_data.csv")    #set path

#define variables for the code
votes_total = 0  
cvotes = 0
candidates = {}
candidatepercent = {}
winner = ""

with open(pollcsv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)   #skip header

   # Read each row of data and add votes for each candidate in the dictionary
    for row in csvreader:
        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1
        #total votes cast
        votes_total = votes_total + 1     

#print(candidates)


# In[35]:


winner = max(candidates, key=candidates.get)  #getting the maximum value in the dictionary

#print(winner)
candidatepercent = {}
# add vote totals and vote %ages to a new dictionary with same key
for key in candidates.keys():
    votes = []
    votes.append(candidates[key]/votes_total * 100)
    votes.append(candidates[key])
    candidatepercent[key] = votes
    #print(candidatepercent)


# In[36]:


#print election results
print("Election Results")
print("-"*69)
print(f"Total Votes: {votes_total}")
print("-"*69)
for key in candidatepercent:
    print(f"{key}: {round(candidatepercent[key][0],3)}% ({candidatepercent[key][1]})")
print("-"*69)
print(f"Winner: {winner}")
print("-"*69)


# In[40]:


#to write the output file
output = os.path.join(".","Analysis", "summary.txt")

# use "\n" to create a new line
with  open(output, 'w') as output:
    output.write("Election Results\n")
    output.write("-"*69 + "\n")
    output.write(f"Total Votes: {votes_total}\n")
    output.write("-"*69 + "\n")
    for key in candidatepercent:
        output.write(f"{key}: {round(candidatepercent[key][0],3)}% ({candidatepercent[key][1]})\n")
    output.write("-"*69 + "\n")
    output.write(f"Winner: {winner}\n")
    output.write("-"*69)

