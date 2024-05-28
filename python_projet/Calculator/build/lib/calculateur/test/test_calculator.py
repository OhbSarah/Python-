import pytest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unittest.mock import patch
from calculateur.calculator import get_numeric_input, get_text_input, calculate, visualize_emission
import calculateur.data

# Sample data to mock the base_sample dataset
sample_data = {
    'Nom base français': ['Avion', 'TGV', 'Voiture particulière', 'Voiture particulière', 'Métro', 'RER', 'Bus', 'Gaz', 'Electricité', 'Repas végétariens', 'Repas avec viande'],
    'Nom attribut français': ['avion', 'TGV', 'essence', 'électrique', 'Métro', 'RER', 'Bus', 'Gaz', 'Electricité', 'végétarien', 'bovine'],
    'Total poste non décomposé': [0.2, 0.1, 0.3, 0.1, 0.05, 0.05, 0.04, 0.3, 0.5, 0.2, 0.5]
}

base_sample = pd.DataFrame(sample_data)

@patch('calculator.input', return_value='42')
def test_get_numeric_input(mock_input):
    assert get_numeric_input("Entrez un nombre: ") == 42.0

@patch('calculator.input', return_value='oui')
def test_get_text_input(mock_input):
    assert get_text_input("Entrez un texte: ", valid_responses=['oui', 'non']) == 'oui'

@patch('calculator.data.load_and_clean_data', return_value=base_sample)
@patch('calculator.get_text_input', side_effect=['électrique', 'électrique'])
@patch('calculator.get_numeric_input', side_effect=[1000, 500, 200, 100, 50, 25, 1000, 2000, 5, 3])
def test_calculate(mock_numeric_input, mock_text_input, mock_load_data):
    detailed_emissions, category_emissions = calculate()
    assert detailed_emissions is not None
    assert category_emissions is not None

def test_visualize_emissions():
    detailed_emissions = {'avion': 200.0, 'TGV': 50.0, 'voiture_électrique': 100.0, 'Métro': 30.0, 'RER': 20.0, 'Bus': 40.0, 'Gaz': 300.0, 'Electricité': 1000.0, 'Repas végétariens': 10.0, 'Repas avec viande': 15.0}
    
    # Use a backend of matplotlib that does not require a GUI
    plt.switch_backend('Agg')
    
    visualize_emissions(detailed_emissions)
    
    # Ensure that no errors occur during plotting
