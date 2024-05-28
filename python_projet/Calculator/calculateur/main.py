''' 
Execution du calculateur d'empreinte carbone
'''

import data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calculator

base_sample=data.load_and_clean_data()
print(base_sample.head())
detailed_emissions = calculator.calculate()

calculator.visualize_emissions(detailed_emissions[1])
