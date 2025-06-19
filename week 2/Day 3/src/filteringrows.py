#  Filter rows based on the selected data

import pandas as pd 

df = pd.read_csv("../../datasets/student.csv")
print(df)

print("\nScored than 80 %\n")
print(df[df['Marks'] > 80])

print("\nGender = Female\n")
print(df[df['gender'] == 'f'])

print("\nGender = Female and place = Kathmandu\n")
print(df[(df['gender'] == 'f') & (df['place'] == 'Kathmandu')])

print("\nNot belongs to place = 'VII' grade\n")
print(df[~(df['Semester'] == 'VII')])


