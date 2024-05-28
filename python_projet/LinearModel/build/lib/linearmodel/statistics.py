'''
    Ce module fournit des fonctions pour effectuer divers calculs statistiques sur des ensembles de données ainsi qu'une class de test statistiques.
    Fonctions disponibles :

        - mean(data) : Retourne la moyenne des données.
        - variance(data) :  Retourne la variance des données.
        - std_deviation(data) : Retourne l'écart-type des données.
        - correlation(x, y) : Retourne le coefficient de corrélation.
        - median(data): Retourne la médiane des données.
        - quantile(data, percentile): Retourne la valeur du quantile pour le percentile spécifié.
        - q1(data): Retourne le premier quartile des données.
        - q3(data): Retourne le Troisième quartile des données.
        - summary(data): Retourne la chaîne de caractères contenant le résumé statistique ou descriptif des données. 
        - table(data1,data2): Retourne la table de contingence.
        - correlation_matrix(data): Retourne un tableau de corrélation.

'''

import pandas as pd

def mean(data):
    '''Calcule de la moyenne
    
    Arguments: data: Dataframe ou list ou tuple
    
    Retourne: int'''
    return sum(data) / len(data)

def variance(data):
    '''calcule de la variance à partir de la moyenne
    
    Arguments: data: Dataframe ou list ou tuple
    
    Retourne: int'''
    mu = mean(data)
    return sum((xi - mu) ** 2 for xi in data) / len(data)

def std_deviation(data):
    '''Calcule de l'écart-type
    
    Arguments: data: Dataframe ou list ou tuple
    
    Retourne: int'''
    return variance(data) ** 0.5

def correlation(x, y):
    '''correlation entre deux variable
    
    Arguments:
    data1 (list): Liste de valeurs numétiques
    data2 (list): Liste de valeurs numétiques.
    
    Retourne: Corrélation entre les 2 listes.
    '''
    mean_x = mean(x)
    mean_y = mean(y)
    numer = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    denom = (sum((xi - mean_x) ** 2 for xi in x) * sum((yi - mean_y) ** 2 for yi in y)) ** 0.5
    return numer / denom

def median(data):
    """
    Calcul de la médiane d'un ensemble de données.

    Arguments:
    data (list): Liste de valeurs numériques.

    Retourne:La médiane des données.
    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        return sorted_data[n // 2]

def quantile(data, percentile):
    """
    Calcul du quantile pour un ensemble de données et un percentile donné.

    Arguments:
        data (list): Liste de valeurs numériques.
        percentile (float): Valeur du percentile.

    Retourne: La valeur du quantile pour le percentile spécifié.
    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    index = int(percentile * (n - 1))
    if index == n - 1:
        return sorted_data[-1]
    return sorted_data[index]

def q1(data):
    """
    Calcul du premier quartile (Q1) d'un ensemble de données.

    Arguments:
        data (list): Liste de valeurs numériques.

    Retourne:Le premier quartile des données.
    """
    return quantile(data, 0.25)

def q3(data):
    """
    Calcul du troisième quartile (Q3) d'un ensemble de données.

    Arguments:
        data (list): Liste de valeurs numériques.

    Retourne:
        Le troisième quartile des données.
    """
    return quantile(data, 0.75)


def summary(data):
    """
    Fonction pour fournir un résumé statistique ou descriptif des données.
    
    Arguments:
        data (pandas.DataFrame): Un DataFrame pandas contenant les données.

    Retourne:
        Une chaîne de caractères contenant le résumé statistique ou descriptif des données.
    """
    quantitative_columns = {}
    qualitative_columns = {}
    for column_name, column_data in data.items():
        if pd.api.types.is_numeric_dtype(column_data):
            quantitative_columns[column_name] = column_data.tolist()
        else:
            qualitative_columns[column_name] = column_data.tolist()

    # Calculer les statistiques descriptives pour les colonnes quantitatives
    quantitative_summary = {}
    for column_name, column_data in quantitative_columns.items():
        column_summary = {
            "Min.": min(column_data),
            "1st Qu.": q1(column_data),
            "Median": median(column_data),
            "Mean": sum(column_data) / len(column_data),
            "3rd Qu.": q3(column_data),
            "Max.": max(column_data),
            "NA's": sum(pd.isna(column_data))
        }
        quantitative_summary[column_name] = column_summary

    # Générer le résumé pour les colonnes quantitatives
    output = ""
    for column_name, stats in quantitative_summary.items():
        output += f"{column_name.ljust(30)}\n"
        for stat, value in stats.items():
            output += f"{stat}: {value:<15} "
        output += "\n"

    # Générer le résumé pour les colonnes qualitatives
    for column_name, column_data in qualitative_columns.items():
        output += f"\n{column_name}:\n"
        unique_values = set(column_data)
        for value in unique_values:
            count = column_data.count(value)
            output += f"{value}: {count} observations\n"

    return output


def correlation_matrix(data):
    """
    Calcule et affiche la matrice de corrélation entre les colonnes numériques d'un DataFrame.

    Arguments:
        data (pandas.DataFrame): Le DataFrame contenant les données.

    Retourne:
        Matrice de corrélation sous forme de DataFrame.
    """
    numeric_columns = data.select_dtypes(include=['float64', 'int64'])

    correlation_matrix = numeric_columns.corr()

    correlation_matrix_df = pd.DataFrame(correlation_matrix, index=numeric_columns.columns, columns=numeric_columns.columns)

    print("Matrice de corrélation entre les colonnes numériques :")
    return correlation_matrix_df 



def table(data1, data2):
    """
    Crée une table de contingence à partir de deux séries de données.

    Arguments:
        data1 (pandas.Series): La première série de données.
        data2 (pandas.Series): La deuxième série de données.

    Retourne:
        pandas.DataFrame: La table de contingence.
    """
    
    df = pd.DataFrame({'Data1': data1, 'Data2': data2})
    
    contingency_table = pd.crosstab(df['Data1'], df['Data2'])
    
    return contingency_table



    

