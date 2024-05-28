# test_reg.py

import pytest
import numpy as np
from linearmodel.reg import OrdinaryLeastSquares

def test_fit():
    model = OrdinaryLeastSquares()
    X = np.array([
        [1, 1],
        [2, 3],
        [3, 5]
    ])
    y = np.array([1, 2, 3])
    model.fit(X, y)
    assert model.coefficients is not None

def test_predict():
    model = OrdinaryLeastSquares()
    X = np.array([
        [1, 1],
        [2, 3],
        [3, 5]
    ])
    y = np.array([1, 2, 3])
    model.fit(X, y)
    predictions = model.predict(X)
    assert predictions is not None
    assert len(predictions) == len(y)

def test_get_coeffs():
    model = OrdinaryLeastSquares()
    X = np.array([
        [1, 1],
        [2, 3],
        [3, 5]
    ])
    y = np.array([1, 2, 3])
    model.fit(X, y)
    coeffs = model.get_coeffs()
    assert coeffs is not None
    assert len(coeffs) == X.shape[1] + 1

def test_calculate_standard_errors():
    model = OrdinaryLeastSquares()
    X = np.array([
        [1, 1],
        [2, 3],
        [3, 5]
    ])
    y = np.array([1, 2, 3])
    model.fit(X, y)
    y_pred = model.predict(X)
    errors = model.calculate_standard_errors(X, y, y_pred)
    assert errors is not None
    assert len(errors) == len(model.coefficients)-1