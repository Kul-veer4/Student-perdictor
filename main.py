import os
import numpy as np
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

# Ensure output folder exists for saved plots
plot_dir = os.path.join(os.path.dirname(__file__), "plots")
os.makedirs(plot_dir, exist_ok=True)

# ======================
# DAY 3: Visualization
# ======================
x = data["study_hours"].to_numpy()
y = data["marks"].to_numpy()

print("\n===== Statistics =====")
print(f"Samples: {len(x)}")
print(f"Study hours: mean={np.mean(x):.2f}, std={np.std(x):.2f}")
print(f"Marks: mean={np.mean(y):.2f}, std={np.std(y):.2f}")

# Scatter with regression line
plt.figure(figsize=(7,5))
plt.scatter(x, y, alpha=0.8, label="data")
if len(x) >= 2:
    coeffs = np.polyfit(x, y, 1)
    poly = np.poly1d(coeffs)
    xs = np.linspace(np.min(x), np.max(x), 100)
    plt.plot(xs, poly(xs), color="red", linestyle="--", label=f"fit: y={coeffs[0]:.2f}x+{coeffs[1]:.2f}")
    corr = np.corrcoef(x, y)[0, 1]
    print(f"Pearson correlation (study_hours, marks): {corr:.3f}")
else:
    print("Not enough data for regression/correlation")

plt.title("Study Hours vs Marks (with linear fit)")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid(True)
plt.legend()
scatter_path = os.path.join(plot_dir, "scatter_with_fit.png")
plt.savefig(scatter_path, bbox_inches="tight")
print(f"Saved scatter plot to: {scatter_path}")
plt.show()

# Histograms
plt.figure(figsize=(10,4))
plt.subplot(1, 2, 1)
plt.hist(x, bins=8, color="#4c72b0", edgecolor="black")
plt.title("Study Hours Distribution")
plt.xlabel("Study Hours")
plt.ylabel("Count")

plt.subplot(1, 2, 2)
plt.hist(y, bins=8, color="#dd8452", edgecolor="black")
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Count")

hist_path = os.path.join(plot_dir, "histograms.png")
plt.tight_layout()
plt.savefig(hist_path, bbox_inches="tight")
print(f"Saved histograms to: {hist_path}")
plt.show()

# Bar chart: mean marks per study-hours bin
bins = np.arange(np.floor(np.min(x)), np.ceil(np.max(x)) + 1)
if len(bins) > 1:
    inds = np.digitize(x, bins, right=False)
    means = [y[inds == i].mean() if np.any(inds == i) else np.nan for i in range(1, len(bins) + 1)]
    centers = bins
    plt.figure(figsize=(7,4))
    plt.bar(centers, means, width=0.8, color="#55a868", edgecolor="black")
    plt.title("Average Marks by Study Hours (binned)")
    plt.xlabel("Study Hours (bin start)")
    plt.ylabel("Average Marks")
    plt.grid(axis="y")
    bar_path = os.path.join(plot_dir, "avg_marks_by_hours.png")
    plt.savefig(bar_path, bbox_inches="tight")
    print(f"Saved binned average bar chart to: {bar_path}")
    plt.show()
else:
    print("Not enough range to compute binned averages for bar chart")

# Insights summary
print("\n===== Insights =====")
if len(x) >= 2:
    if corr > 0.6:
        print("Strong positive relationship: more study hours are associated with higher marks.")
    elif corr > 0.3:
        print("Moderate positive relationship between study hours and marks.")
    elif corr > 0:
        print("Weak positive relationship between study hours and marks.")
    else:
        print("Little to no positive linear relationship detected.")
else:
    print("Insufficient data to draw robust insights.")

print("Done: Day 3 visualizations and insights.")