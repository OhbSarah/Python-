# test_visualization.py

import pytest
import numpy as np
import matplotlib.pyplot as plt
import linearmodel.statistics
from linearmodel.visualization import plot_residuals_vs_fitted, qqplot

def test_plot_residuals_vs_fitted():
    # Données de test
    fitted_values = np.array([1.1, 1.9, 3.2, 3.8, 5.1])
    residu = np.array([0.1, -0.1, 0.2, -0.2, 0.1])
    
    # Utiliser un backend de matplotlib qui ne nécessite pas d'interface utilisateur
    plt.switch_backend('Agg')
    
    # Appeler la fonction de tracé
    plot_residuals_vs_fitted(fitted_values, residu)
    


