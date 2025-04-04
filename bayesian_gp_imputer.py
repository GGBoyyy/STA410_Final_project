#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# bayesian_gp_imputer.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C

class BayesianGPImputer:
    def __init__(self, kernel=None, alpha=1e-5):
        if kernel is None:
            kernel = C(1.0, (1e-3, 1e3)) * RBF(length_scale=1.0, length_scale_bounds=(1e-2, 1e2))
        self.kernel = kernel
        self.alpha = alpha
        self.gp = GaussianProcessRegressor(kernel=self.kernel, alpha=self.alpha, normalize_y=True)

    def fit(self, X, y):
        X = np.array(X).reshape(-1, 1)
        y = np.array(y)
        self.gp.fit(X, y)

    def impute(self, X_all):
        X_all = np.array(X_all).reshape(-1, 1)
        y_pred, sigma = self.gp.predict(X_all, return_std=True)
        return y_pred, sigma

    def plot_imputation(self, X_train, y_train, X_all, y_imputed, sigma):
        plt.figure(figsize=(10, 5))
        plt.plot(X_all, y_imputed, 'b-', label='Imputed')
        plt.fill_between(X_all.ravel(), y_imputed - 1.96 * sigma, y_imputed + 1.96 * sigma, color='blue', alpha=0.2, label='95% CI')
        plt.scatter(X_train, y_train, color='red', label='Observed')
        plt.title('Bayesian GP Imputation of Missing Financial Data')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

