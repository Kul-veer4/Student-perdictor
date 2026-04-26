import pandas as pd
import matplotlib.pyplot as plt

# ======================
# DAY 1: Load Data
# ======================
try:
    data = pd.read_csv("data.csv")
except FileNotFoundError:
    print("Error: data.csv file not found!")
    exit()

print("===== Original Data =====")
print(data)

# ======================
# DAY 2: Data Cleaning
# ======================
print("\n===== Missing Values =====")
print(data.isnull().sum())

# Remove missing values
data = data.dropna()

print("\n===== Cleaned Data =====")
print(data)

# ======================
# DAY 3: Visualization
# ======================
plt.figure(figsize=(6,4))

plt.scatter(data["study_hours"], data["marks"])

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.grid(True)

plt.show()