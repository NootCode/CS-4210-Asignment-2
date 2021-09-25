#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

#reading the training data
#--> add your Python code here
db = []
with open('Question 5\weather_training.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
#transform the original training features to numbers and add to the 4D array X. For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
#X =
#KEY 
# Sunny = 1         Cool = 1        Normal = 1      Weak = 1        Yes = 1
# Overcast = 2      Mild = 2        High = 2        Strong = 2      No = 2
# Rain = 3          Hot = 3
X = []
Y = []
for instance in db:
    row = []
    for num, att in enumerate(instance):
        if(num != 0 or num != len(instance)-1):
            if(att == "Sunny"):
                row.append(1)
            elif(att == "Rain"):
                row.append(3)
            elif(att == "Overcast"):
                row.append(2)
            elif(att == "Hot"):
                row.append(3)
            elif(att == "Mild"):
                row.append(2)
            elif(att == "Cool"):
                row.append(1)
            elif(att == "High"):
                row.append(2)
            elif(att == "Normal"):
                row.append(1)
            elif(att == "Strong"):
                row.append(2)
            elif(att == "Weak"):
                row.append(1)
        if (num == len(instance) -1):
            if(att == "Yes"):
                Y.append(1)
            else:
                Y.append(2)
    X.append(row)

#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
# Y =

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the data in a csv file
#--> add your Python code here
test_samples = []
with open('Question 5\weather_test.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         test_samples.append (row)

#printing the header os the solution
print ("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))

#use your test samples to make probabilistic predictions.
#--> add your Python code here
#-->predicted = clf.predict_proba([[3, 1, 2, 1]])[0]

for instance in test_samples:
    row = []
    for num, att in enumerate(instance):
        if(num != 0):
            if(att == "Sunny"):
                row.append(1)
            elif(att == "Rain"):
                row.append(3)
            elif(att == "Overcast"):
                row.append(2)
            elif(att == "Hot"):
                row.append(3)
            elif(att == "Mild"):
                row.append(2)
            elif(att == "Cool"):
                row.append(1)
            elif(att == "High"):
                row.append(2)
            elif(att == "Normal"):
                row.append(1)
            elif(att == "Strong"):
                row.append(2)
            elif(att == "Weak"):
                row.append(1)
    this_inst = []
    this_inst.append(row)
    #print(this_inst)
    predicted = clf.predict_proba(this_inst)[0]
    if(predicted[0] >= .75):
        print(instance[0].ljust(15) + instance[1].ljust(15) + instance[2].ljust(15) + instance[3].ljust(15) + 
        instance[4].ljust(15) + "Yes".ljust(15) + str(predicted[0]).ljust(15))
    if(predicted[1] >= .75):
        print(instance[0].ljust(15) + instance[1].ljust(15) + instance[2].ljust(15) + instance[3].ljust(15) + 
        instance[4].ljust(15) + "No".ljust(15) + str(predicted[1]).ljust(15))
    


