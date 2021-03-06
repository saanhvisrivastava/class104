# -*- coding: utf-8 -*-
"""class104.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QI0X_1D2YRs7GCkJ1IE2NQBzi9ii0Chb
"""

#Calculate mean
import csv
with open("Data.csv",newline="") as f :
  reader=csv.reader(f)
  file_data=list(reader)
#print(file_data)
file_data.pop(0)
#print(file_data)
new_data=[]
for i in range(len(file_data)):
  n_num=file_data[i][1]
  new_data.append(float(n_num))
print(new_data)

n=len(new_data)
total=0
for i in new_data:
  total+=i

mean=total/n
print("Mean average is"+ str(mean))

#To calculate median
import csv
with open("Data.csv",newline="") as f :
  reader=csv.reader(f)
  file_data=list(reader)
#print(file_data)
file_data.pop(0)
#print(file_data)
new_data=[]
for i in range(len(file_data)):
  n_num=file_data[i][1]
  new_data.append(float(n_num))
  #To find the length os the data
n=len(new_data)
new_data.sort()

if n%2==0 :
  median1=float(new_data[n//2])
  median2=float(new_data[n//2-1])
  sum=median1+median2
  median=sum/2
#print(median)

else:
  median=float(new_data[n//2])
print("Median is "+ str(median))

from collections import Counter
import csv

with open('Data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
	n_num = file_data[i][1]
	new_data.append(n_num)



#Calculating Mode
data = Counter(new_data)
mode_data_for_range = {
                        "50-60": 0,
                        "60-70": 0,
                        "70-80": 0
                    }
for height, occurence in data.items():
    if 50 < float(height) < 60:
        mode_data_for_range["50-60"] += occurence
    elif 60 < float(height) < 70:
        mode_data_for_range["60-70"] += occurence
    elif 70 < float(height) < 80:
        mode_data_for_range["70-80"] += occurence

mode_range, mode_occurence = 0, 0
for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"Mode is -> {mode:2f}")

