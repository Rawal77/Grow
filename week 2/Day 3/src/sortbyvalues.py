# Sort the DataFrame by two columns and reset the index

import pandas as pd 

df = pd.read_csv('../../datasets/student.csv')

print(df.info())

print(df.head())

print("\n Sorted values based by marks (Default)\n")
print(df.sort_values(by=['Marks']))

print("\n Sorted values based by marks \n")
print(df.sort_values(by=['Marks'], ascending=[False]))

print("\n Sorted values based by marks and name (Default)\n")
print(df.sort_values(by=['Marks','Name']))



print("\n Putting index as a name\n")
df.set_index('Name',inplace=True)
print(df)

print("\n Removing index as a name\n")
df.reset_index(drop = True,inplace=True)
print(df)
