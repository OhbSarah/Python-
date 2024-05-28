# test_statistics.py

import pytest
import pandas as pd
import numpy as np
from linearmodel.statistics import (mean, variance, std_deviation, correlation, quantile, summary)

def test_mean():
    data = [1, 2, 3, 4, 5]
    assert mean(data) == 3

def test_variance():
    data = [1, 2, 3, 4, 5]
    assert variance(data) == 2.0

def test_std_deviation():
    data = [1, 2, 3, 4, 5]
    assert std_deviation(data) == pytest.approx(1.4142, 0.0001)

def test_correlation():
    x = [1, 2, 3, 4, 5]
    y = [5, 4, 3, 2, 1]
    assert correlation(x, y) == -1

def test_quantile():
    data = [1, 2, 3, 4, 5]
    assert quantile(data, 0.5) == 3

def test_summary():
    data = pd.DataFrame({
        'A': [1, 2, 3, 4, 5, None],
        'B': ['a', 'b', 'a', 'b', 'a', 'b'],
        'C': [10.5, 22.3, 13.1, 44.0, 15.2, 18.3]
    })

    result = summary(data)
    
    expected_output = (
        "A                             \n"
        "Min.: 1                      1st Qu.: 1.75         Median: 3.0          Mean: 3.0          3rd Qu.: 4.25         Max.: 5.0          NA's: 1             \n"
        "C                             \n"
        "Min.: 10.5                   1st Qu.: 13.1         Median: 16.75        Mean: 20.566666666666666 3rd Qu.: 22.3         Max.: 44.0         NA's: 0             \n"
        "\n"
        "B:\n"
        "a: 3 observations\n"
        "b: 3 observations\n"
    )
    
    # Comparer les premières lignes pour valider le format du résumé.
    assert result.startswith("A"), "Le résumé devrait commencer par la colonne 'A'."
    assert "Min.: 1" in result, "Le résumé devrait contenir les statistiques de base pour la colonne 'A'."
    assert "B:\n" in result, "Le résumé devrait contenir les observations pour la colonne 'B'."
    assert "a: 3 observations\n" in result, "Le résumé devrait compter correctement les valeurs de 'B'."
    assert "b: 3 observations\n" in result, "Le résumé devrait compter correctement les valeurs de 'B'."


