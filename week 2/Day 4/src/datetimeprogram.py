import pandas as pd

df = pd.DataFrame({
    'Date': ['2025-01-03', '2025-01-01', '2025-01-02'],
    'Value': [15, 10, 12]
})

df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
df = df.sort_index()

print(df)
print("Is datetime index monotonic?:", df.index.is_monotonic_increasing)
