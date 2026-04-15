# 🌊 Flood Early Warning System

A machine learning project that predicts district-level flood risk from historical rainfall data — turning unused meteorological records into actionable early warnings for local governments.

---

## The Problem

Local governments often fail to anticipate rainfall-induced flooding because decades of historical rainfall data sits unused. By the time the scale of an event becomes clear, evacuation windows have already closed. This project addresses that gap by building a predictive system that learns from historical patterns and flags flood risk before an event occurs.

---

## What This Project Does

This system takes historical rainfall data for a region and predicts whether conditions represent a flood risk. It outputs a risk level — High, Medium, or Low — along with a probability score and a recommended government action. The goal is to give district officials enough lead time to act.

---

## Approach

The project follows the complete data science lifecycle from raw data to prediction:

**Data Cleaning** — Raw rainfall records are cleaned for missing values, duplicates, and inconsistent formats before any analysis begins.

**Exploratory Analysis** — The data is examined visually and statistically to understand rainfall distributions, seasonal patterns, regional differences, and correlations. This step confirms that the June–September monsoon season is the dominant driver of flood risk across most regions.

**Feature Engineering** — New variables are derived from the raw monthly data, including seasonal rainfall totals, monsoon intensity flags, and a rainfall anomaly score that measures how far a given year deviates from the long-term historical average.

**Predictive Modelling** — A Decision Tree classifier is trained to predict flood risk based on the engineered features. The model is evaluated primarily on Recall — the proportion of actual flood-risk years it correctly identifies — because missing a genuine flood event is far more dangerous than issuing a false alarm.

**Early Warning Function** — The trained model is wrapped in a prediction function that accepts district rainfall conditions and returns a formatted risk report with recommended action.

---

## Key Findings

- Monsoon season (June–September) accounts for over 75% of annual rainfall across most regions, making monsoon intensity the primary flood risk signal
- A rainfall anomaly score — how far a year's rainfall sits from the historical mean — is the strongest single predictor of flood risk
- Coastal and north-eastern subdivisions show the highest historical flood-risk frequency
- Long-term data reveals a gradual upward trend in extreme rainfall years, consistent with climate change projections

---

## Model

The classifier used is a Decision Tree, chosen for its interpretability — a district official can trace exactly why a warning was issued. The model is trained on 80% of the data and evaluated on the remaining 20%, with 5-fold cross-validation used to confirm stability across different data splits.

Recall on flood-risk years is the headline performance metric.

---

## Assumptions

- Missing monthly rainfall values are treated as zero rainfall rather than recording errors
- A year is classified as high flood risk if its annual rainfall exceeds the 75th percentile of the historical distribution
- Historical patterns from the dataset are assumed to be reasonably representative of near-future conditions

---

## Limitations

- The model is trained on annual, regional-level data. A production early warning system would require daily or hourly readings at the district level
- River gauge levels — the most direct precursor to flooding — are not included in this dataset
- The flood risk label is derived from a rainfall threshold, not from actual recorded flood event data
- The model will need periodic retraining as climate patterns shift over time

---

## Technologies Used

Python · Pandas · NumPy · Matplotlib · Seaborn · Scikit-learn · Jupyter Notebook

---

## Local Environment Setup

Use Conda to create the project environment and verify tools before starting notebooks:

```bash
conda env create -f environment.yml
conda activate hydroguard
python scripts/verify_python_tools.py
```

This keeps local development consistent across Python scripts and Jupyter workflows used in upcoming learning units.

To launch Jupyter directly in the project notebook workspace:

```bash
python scripts/launch_jupyter.py
```

---

## Project Structure

```text
S66_0426_StrataLabs_DATASCIENCE_HydroGuard2/
|- data/
|  |- raw/
|  |- processed/
|- notebooks/
|- outputs/
|- scripts/
|- src/
```

This structure separates immutable source data, transformed data, reusable code, and generated artifacts so the full pipeline remains auditable.

To move the sample rainfall file from raw stage to processed stage:

```bash
python scripts/stage_rainfall_data.py
```

To run the first script-based rainfall analysis and generate a report:

```bash
python scripts/first_data_analysis.py
```

To run numeric/string parsing demo for rainfall inputs:

```bash
python scripts/numeric_string_demo.py
```

To run data-structure demo for district rainfall summaries:

```bash
python scripts/data_structures_demo.py
```

To run conditional risk classification from monsoon totals:

```bash
python scripts/conditional_risk_demo.py
```

To run loop-based iterative rainfall processing:

```bash
python scripts/iterative_processing_demo.py
```

To run function definition/call demo for rainfall summaries:

```bash
python scripts/functions_demo.py
```

To run function input/output anomaly demo:

```bash
python scripts/function_io_demo.py
```

To run readable naming and PEP 8 style demo:

```bash
python scripts/readable_style_demo.py
```

To run structured reusable pipeline demo:

```bash
python scripts/structured_pipeline_demo.py
```

To run NumPy array creation demo from Python lists:

```bash
python scripts/numpy_array_creation_demo.py
```

To run NumPy shape and index inspection demo:

```bash
python scripts/numpy_shape_index_demo.py
```

To run basic NumPy mathematical operations demo:

```bash
python scripts/numpy_math_operations_demo.py
```

To run vectorized NumPy anomaly calculations:

```bash
python scripts/numpy_vectorization_demo.py
```

To run NumPy broadcasting demo:

```bash
python scripts/numpy_broadcasting_demo.py
```

To run pandas Series creation demo:

```bash
python scripts/pandas_series_creation_demo.py
```

To run pandas DataFrame creation demo:

```bash
python scripts/pandas_dataframe_creation_demo.py
```

To run pandas CSV loading demo:

```bash
python scripts/pandas_csv_loading_demo.py
```

To run DataFrame inspection demo:

```bash
python scripts/pandas_inspection_demo.py
```

To run DataFrame shape and dtype inspection demo:

```bash
python scripts/pandas_shape_dtypes_demo.py
```

To run pandas indexing and slicing demo:

```bash
python scripts/pandas_indexing_demo.py
```

---
