import pandas as pd

df = pd.DataFrame({
    'Name': ['Ram', 'Shyam', 'Hari', 'Gita'],
    'Age': [25, None, 30, None],
    'Salary': [50000, 60000, None, None]
})

critical_cols = ['Age', 'Salary']

df_cleaned = df.dropna(subset=critical_cols)
print(df)

print(df_cleaned)
