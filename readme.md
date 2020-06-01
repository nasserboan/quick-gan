
# TITLE

## SUBTITLE 1 

## SUBTITLE 2

## Project Structure

```

├── readme.md          <- The top-level README.
│
├── data
│   ├── final          <- Model-ready dataset.
│   ├── intermediate   <- Intermediate data for EDA and data preparation.
│   └── raw            <- The original, immutable data dump.
│
├── models             <- Trained models.
│
├── notebooks          <- Jupyter notebooks
│
├── reports            <- Reports created.
│
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── make_features.py
│   │
│   └── models         <- Scripts to train models and then use trained models to make predictions
│       └── train_model.py
│
└── environment.yml    <- The yml file for setting up the conda environment with all requirements.

```