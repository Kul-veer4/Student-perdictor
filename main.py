import pandas as pd

data = pd.read_csv("data.csv")

print("Original Data:")
print(data)

# Check missing values
print("\nMissing values:")
print(data.isnull().sum())

# Remove missing values (if any)
data = data.dropna()

print("\nCleaned Data:")
print(data)