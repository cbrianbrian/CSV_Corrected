'''
Brian Casillas 08/14/2025

This code:
- corrects .csv files to right number of columns
    ex) column with 2 data sets per cell A1 = [0,1] (wrong) 
    to 2 columns with 1 data set per cell A1 = [0], B1 = [1] (correct)
- Option to save using CSV module or Pandas

**Comment and uncomment lines of code as necessary**

'''

import csv
import pandas as pd

csvname = input('Paste .csv file name to analyze: ') #Exclude .csv
csvname = f"{csvname}.csv"

#UNCOMMENT IF CSV IN DIFFERENT DIRECTORY THAN CODE
'''
def pathname(csv_name):
    directory = input('Paste directory path: ')

    path = f"{directory}\\{csv_name}"
    return path

csvname = pathname(csvname)   
'''

#csv to list 
a = []
with open(csvname, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        a.append(row[0]) #appending cell>array>value(s) to empty list 'a'

#corrected list splits 2 items to get 2 arrays per cell      
newdata = []
for i in range(len(a)):
    newdata.append(a[i].split(','))

'''
# Save the modified DataFrame to a new CSV file using PANDAS
csvname = csvname[:-4] #Removes '.csv' from file name
df = pd.DataFrame(newdata)
df.to_csv(f"{csvname}_clean.csv", index=False, header=False) #header=False to remove 0 and 1 from csv columns
'''

# Save the modified DataFrame to a new CSV file using python's built in CSV module
csvname = csvname[:-4] #Removes '.csv' from file name
with open(f"{csvname}_clean.csv" , 'w', newline='') as csvfile: #newline = '' to avoid writing data every other row and keep it consecutive
    writer = csv.writer(csvfile)
    writer.writerows(newdata)


  
        


    