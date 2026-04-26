# Student Predictor

This project demonstrates an end-to-end student performance predictor built in Python.

Overview
- Day 1: Load dataset from `data.csv` using `pandas` and inspect it.
- Day 2: Clean the data (drop / handle missing values).
- Day 3: Visualize relationships with `matplotlib` (scatter, histograms, binned averages).
- Day 4: Train a linear regression model to learn marks from study hours.
- Day 5: Use the trained model to predict marks from user input.
- Final: Integrate components and push the project to GitHub.

Files
- `main.py` — data loading, cleaning, visualization, and insights.
- `data.csv` — dataset (study_hours, marks).
- `plots/` — generated plot images (created when running `main.py`).

Quick start

1. Create a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows: .venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the script to generate visualizations:

```bash
python main.py
```

Notes
- If you want to run prediction (linear regression), install `scikit-learn` and run the model-training steps (not included in `main.py` visualization-only flow).

License
- MIT
