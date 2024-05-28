''' 
    Class OrdinaryLeastSquares permettant de tracer une regression linéaire par moindre carré.
    Methode constituant la class:
    - fit : Calcule l'estimateur des moindres carrés.
    - predict: Retourne les predictions du modéle
    - get_coeffs: Retourne les coefficients estimés
    - calculate_standard_errors: Retourne les erreurs standards associées aux coefficients
    - calculate_t_statistics: Retourne les statistique de test t-test
    - coefficient_determination: Retourne le coefficient de determination
    - _print_results : Affiche les coefficients, leurs erreurs et leur statistiques de test associé ainsi que le coefficient de determination
    - visualise_result : Affiche sur un même graphique les observation et les predictions
    -  visualiser : Affiche un nuage de points des predictions selon les observations
    '''

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings
import statistics

class OrdinaryLeastSquares:
    def __init__(self, intercept=True):

        self.intercept = intercept
        self.coefficients = None


    def fit(self, X, y):
        """
        Calcule l'estimateur des moindres carrés.

        Arguments:
        :param X: Matrice de données d'entraînement de dimension (n, d)
        :param y: Vecteur cible de dimension (n,)
        """
        # Ajout d'une colonne de 1 pour le terme constant dans X
        X_with_intercept = np.column_stack((np.ones(len(X)), X))
        self.coefficients = np.linalg.inv(X_with_intercept.T @ (X_with_intercept))@(X_with_intercept.T)@(y)

    def predict(self, X):
        '''
        Calcule les predictions de la variable à expliquer suivant le modele établie

        Argument:
            X: Matrice contenant les variables explicatives

        Retourne: vecteur des predictions
        '''
        
        if self.coefficients is None:
            print("Le modèle n'est pas encore ajusté.")
            return
            
    # S'assurer que X est un tableau 2D
        if isinstance(X, pd.Series):
            X = X.values.reshape(-1, 1)
        elif isinstance(X, pd.DataFrame):
            X = X.values
        
        X_with_intercept = np.hstack((np.ones((X.shape[0], 1)), X))
    
        y_pred = X_with_intercept @ self.coefficients  
        return y_pred


    def get_coeffs(self):
        """
        Retourne les valeurs des coefficients estimés.

        Retourne: Vecteur des coefficients estimés
        """
        return self.coefficients

    
    def calculate_standard_errors(self, X, y, y_pred):
        """
        Calcule les erreurs standards à partir des résidus et de la matrice de conception.

        Arguments
        X: Matrice de conception du modèle
        y= Vecteur contenant les valeurs de la variable à expliquer
        y_pred= Vecteur de prédictions
        
        Retourne: Vecteur des erreurs standards
        """
        residuals=y-y_pred
        n, k = X.shape
        sigma_squared = np.sum(residuals ** 2) / (n - k)  # Variance des résidus
        covariance_matrix = np.linalg.inv(X.T @ X) * sigma_squared  # Matrice de covariance
        standard_errors = np.sqrt(np.diag(covariance_matrix))  
        return standard_errors


    def calculate_t_statistics(self,coefficients, standard_errors):
        """
        Calcule les statistiques t à partir des coefficients estimés et de leurs erreurs standards.

        Arguments:
        coefficients: Vecteur des coefficients estimés
        standard_errors: Vecteur des erreurs standard
        
        Retourne: Vecteur des statistiques t
        """
         
        return coefficients / standard_errors
        
        
    def coefficient_determination(self, X, y):
        ''' 
        Calcule le coefficient de determination
        '''
        if self.coefficients is None:
            print("Le modèle n'est pas encore ajusté.")
            return None
        X = np.hstack((np.ones((X.shape[0], 1)), X))
        y_pred = X @ self.coefficients
        ss_total = np.sum((y - np.mean(y)) ** 2)
        ss_residual = np.sum((y - y_pred) ** 2)
        r_squared = 1 - (ss_residual / ss_total)
        return r_squared

    def _print_results(self,X,y,y_pred):
        """
        Affiche les résultats de l'estimation des moindres carrés.

        X: Matrice de conception du modèle
        y= Vecteur contenant les valeurs de la variable à expliquer
        y_pred= Vecteur de prédictions

        Retourne: un sommaire des resultats
        """
        print("Intercept:")
        print(f'{self.coefficients[0]}\n')
        print(f'Coefficients : {self.coefficients[1:]}\n')
        print(f'std_error:{self.calculate_standard_errors(X,y,y_pred)}\n')
        err=self.calculate_standard_errors(X,y,y_pred)
        print(f't stat {self.calculate_t_statistics(self.coefficients[1:],err)}\n')
        print(f'Coefficient de détermination: {self.coefficient_determination(X, y)}')

    def visualise_result(self, X, y):
        '''
         Affiche sur un graphique les resultats de la prédiction et des observations
       
         X: Matrice de conception du modèle
         y= Vecteur contenant les valeurs de la variable à expliquer
        
        '''
        plt.plot( np.arange(stop=np.size(X[:, 0])),self.predict(X),"-r",np.arange(stop=np.size(X[:, 0])),y, )
        plt.title("Représentation du modèle")
        plt.xlabel("index")
        plt.ylabel("y")
        plt.legend(labels=["Prédiction", "Observation"])    
        plt.savefig('Prediction-Observation')
        plt.show()

    def visualiser(self, X, y):
        '''
        Affiche un nuage de points des prédictions selon les observation
       
        X: Matrice de conception du modèle
        y= Vecteur contenant les valeurs de la variable à expliquer
        
        '''
        if self.coefficients is None:
            print("Le modèle n'est pas encore ajusté.")
            return

        if isinstance(y, pd.Series):
            y = y.values.reshape(-1, 1)
            
        if isinstance(X, pd.Series):
            X = X.values.reshape(-1, 1)
        elif isinstance(X, pd.DataFrame):
            X = X.values
        
        X_with_intercept = np.hstack((np.ones((X.shape[0], 1)), X))
    
        y_pred = X_with_intercept @ self.coefficients  # Ajouter l'intercept
    
        plt.figure(figsize=(10, 6))
        plt.scatter(y, y_pred, color='blue')
        plt.plot([y.min(), y.max()], [y.min(), y.max()], linestyle='--', color='red')
        plt.xlabel('y Réel')
        plt.ylabel('y Prédit')
        plt.title('Régression Linéaire - Moindres Carrés')
        plt.savefig('Régression Linéaire - Moindres Carrés')
        plt.show()

