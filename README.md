# STA410_Final_project
# Bayesian Imputation for Missing Financial Data

This project demonstrates a Bayesian approach to imputing missing values in financial time series data using **Gaussian Processes (GPs)**. The methodology is implemented in a clean Python module and demonstrated through Jupyter notebooks.

## 📦 Project Structure
```
STA410_Final_project/
├── bayesian_gp_imputer.py       # Main imputer class using GPs
├── demo_imputation.ipynb     # Demo: simulate data, introduce NaNs, impute with GP
├── methodology_explained.ipynb # Theory & explanation of Bayesian GP imputation
├── tesla-stock-price.csv  # Tesla stock price from public
├── README.md
```

## 📈 What It Does
- Simulates or loads financial time series data
- Introduces missing values
- Uses Bayesian Gaussian Process regression to impute missing values
- Visualizes both predictions and uncertainty intervals

## 🧠 Why Gaussian Processes?
- Flexibly model smooth time series patterns
- Quantify **uncertainty** in imputed values
- Fully Bayesian, interpretable and principled

## 🚀 Getting Started
### 1. Clone and install dependencies
```bash
git clone https://github.com/GGBoyyy/STA410_Final_project.git
cd STA410_Final_project
pip install -r requirements.txt
```

### 2. Run the demo notebook
Open `demo_imputation.ipynb` to:
- See how missing values are introduced
- Watch the imputer in action
- Visualize uncertainty bounds

### 3. Explore the methodology
Open `methodology_explained.ipynb` to understand the math and rationale behind the approach.

## 📚 Requirements
- Python 3.8+
- `numpy`, `pandas`, `scikit-learn`, `matplotlib`

(Install using `pip install -r requirements.txt` or manually.)

## ✨ Future Extensions
- Multivariate GP imputation
- Real-world financial datasets (e.g., Yahoo Finance)
- Kernel tuning and model selection



