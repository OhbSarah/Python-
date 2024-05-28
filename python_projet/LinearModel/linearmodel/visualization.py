'''
    Ce module fournit des fonctions pour visualiser les données.
    Fonctions disponibles :

        - plot_histogram : Retourne un histogramme
        - plot_boxplot: Retourne un boxplot
        - plot_scatter: Retourne un nuage de point
        - plot_pairs: Retourne les nuages de points des différentes correlation
        - plot_residuals_vs_fitted: Retourne un nuage de point des résidues
        -qqplot: Retourne qqplot

'''
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import statistics


def plot_histogram(data, bins=30, title='Histogram', xlabel='Values', ylabel='Frequency'):
    '''
    Affiche un histogramme
    Argument: 
    -Liste ou series 
    -Etendus des barres par défaults à 30 
    -Titre 
    -legende axe des abscisses
    -légende axe des ordonnées
    '''
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=bins, color='skyblue', edgecolor='black')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.savefig('histogram')
    plt.show()

def plot_boxplot(data, columns):
    '''
    Affiche un boxlot
    Argument: 
    -Base de données 
    -colonne de la base de données dont ou veut un boxplot 
    '''
    plt.figure(figsize=(10, 8))
    for i, column in enumerate(columns, start=1):
        plt.subplot(1, len(columns), i)
        plt.boxplot(data[column].dropna())
        plt.title(f'Boxplot de la colonne "{column}"')
        plt.xlabel(column)
    plt.tight_layout()
    plt.savefig(f'{column}_boxplot.png')
    plt.show()

def plot_scatter(data, x_column, y_column):
    """
    Affiche un nuage de points pour deux colonnes spécifiées dans les données.

    Arguments :
    - data : DataFrame, les données
    - x_column : str, nom de la colonne pour l'axe des abscisses
    - y_column : str, nom de la colonne pour l'axe des ordonnées
    """
    if x_column not in data.columns or y_column not in data.columns:
        raise ValueError(f"Les colonnes spécifiées ({x_column}, {y_column}) n'existent pas dans le DataFrame.")

    x_values = data[x_column].dropna()
    y_values = data[y_column].dropna()

    plt.figure(figsize=(10, 6))
    plt.scatter(x_values, y_values, color='black', alpha=0.7, edgecolors='w', s=100)
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f'Nuage de points entre {x_column} et {y_column}')
    plt.grid(True)
    plt.savefig(f'{x_column}_vs_{y_column}_nuage_de_point.png')
    plt.show()

def plot_pairs(df):
    '''
    Affiche les correlations par paire sous forme de nuage de point
    Arquments:
    -Données(DataFrame)
    '''
    warnings.filterwarnings("ignore")
    # Créer une grille de nuages de points pour toutes les paires de colonnes
    sns.set(style="whitegrid")
    pair_plot = sns.pairplot(df)
    pair_plot.fig.suptitle("Nuages de points de corrélation pour toutes les paires de colonnes", y=1.02)
    plt.savefig('Correlation 2 à 2 ')
    plt.show()

def plot_residuals_vs_fitted(fitted_values, residu):
    """
    Trace un nuage de points "Residuals vs Fitted".

    Arguments :
        fitted_values (array-like) : Les valeurs ajustées par le modèle.
        residuals (array-like) : Les résidus calculés comme la différence entre les valeurs observées et les valeurs prédites.

    Retourne :
        None
    """
    plt.figure(figsize=(8, 6))
    plt.scatter(fitted_values, residu, color='blue', alpha=0.7)
    plt.axhline(y=0, color='red', linestyle='--')
    plt.title('Residuals vs Fitted')
    plt.xlabel('Fitted values')
    plt.ylabel('Residuals')
    plt.grid(True)
    plt.savefig('residuals_vs_fitted')
    plt.show()


def erfinv(x, terms=10):
    """
    Approximation de la fonction inverse de l'erreur par une série de Taylor.

    Arguments:
        x : Valeur pour laquelle l'approximation est souhaitée.
        terms : Nombre de termes à utiliser dans la série de Taylor.

    Retourne:
     Approximation de erfinv(x).
    """
    # Coefficients de la série de Taylor pour erfinv
    coefficients = [1.0, 1.0 / 3, 1.0 / 10, 1.0 / 42, 1.0 / 216, 1.0 / 1320, 1.0 / 9360]

    # Constante de la série de Taylor
    constant = 2 / np.sqrt(np.pi)

    # Limiter le nombre de termes au maximum de termes disponibles
    max_terms = len(coefficients)
    terms = min(terms, max_terms)

    # Approximation de erfinv(x) par la série de Taylor
    result = 0
    for n in range(terms):
        result += coefficients[n] * ((np.sqrt(np.pi) / 2) * x) ** (2 * n + 1)

    return constant * result

def get_distribution_params(distribution, size, dist_params):
    """
    Fonction pour générer les quantiles théoriques basés sur la distribution et les paramètres donnés.

    Arguments:
    distribution : La distribution théorique (normale, exponentielle, uniforme).
    size : Taille des données.
    dist_params : Paramètres de la distribution.

    Retourne:
      Quantiles théoriques.
    """
    quantiles = np.linspace(0, 1, size)

    if distribution == 'norm':
        mean, std = dist_params
        theoretical_quantiles = mean + std * np.sqrt(2) * erfinv(2 * quantiles - 1)
    elif distribution == 'expon':
        scale, = dist_params
        theoretical_quantiles = -scale * np.log(1 - quantiles)
    elif distribution == 'uniform':
        low, high = dist_params
        theoretical_quantiles = low + (high - low) * quantiles
    else:
        raise ValueError(f"Distribution '{distribution}' non supportée.")

    return theoretical_quantiles

def qqplot(data, distribution='norm', dist_params=()):
    """
    Trace un Q-Q plot pour vérifier si les données suivent une distribution spécifiée.

    Arguments:
    data : Les données à vérifier.
    distribution : La distribution théorique à comparer (norm, expon, uniform).
    dist_params : Paramètres supplémentaires pour la distribution spécifiée.

    Retourne:
    None
    """
    # Calculer les quantiles empiriques en utilisant la fonction quantile
    quantiles = np.linspace(0, 1, len(data))
    empirical_quantiles = [statistics.quantile(data, q) for q in quantiles]

    # Calculer les quantiles théoriques en fonction de la distribution spécifiée
    theoretical_quantiles = get_distribution_params(distribution, len(data), dist_params)

    # Tracer le Q-Q plot
    plt.figure(figsize=(8, 6))
    plt.plot(theoretical_quantiles, empirical_quantiles, 'o', label='Données')
    plt.plot(theoretical_quantiles, theoretical_quantiles, 'r--', label='Ligne de référence')
    plt.xlabel('Quantiles théoriques')
    plt.ylabel('Quantiles empiriques')
    plt.title(f'Q-Q Plot par rapport à une distribution {distribution}')
    plt.legend()
    plt.grid(True)
    plt.savefig('QQ-Plot')
    plt.show()
