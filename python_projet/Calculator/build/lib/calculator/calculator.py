'''
Permet de calculer l'empreinte carbone annuelle
Les fonction disponible sont :
    -get_numeric_input
    -get_text_input
    -calculate : Retourne l'empreinte carbone selon les différentes sous categories et selon les grandes categories
    -visualize_emissions : Retourne un barplot qui affiche l'empreinte carbone selon les grandes categories
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import load_data

base_sample=load_data.load_and_clean_data()

def get_numeric_input(prompt):
    '''
    Recupere les reponse numerique
    '''
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def get_text_input(prompt, valid_responses=None):
    '''
    Recupere les reponses non numerique (texte)
    '''
    while True:
        answer = input(prompt).strip().lower()
        if valid_responses is None or answer in valid_responses:
            return answer
        print(f"Veuillez entrer une réponse valide parmi les options suivantes : {', '.join(valid_responses)}.")

def calculate():
    '''
    Permet de calculer l'empreinte carbone selon différentes categories grâce aux données
    Demande à l'utilisateur de rentrer ses consommations suivant les questions
    Calcule les emission par categories puis l'empreinte carbone annuelle total

    Retourne: Emission annuelle total et par categorie
    '''

    questions = {
        "transport": {
            "avion": "Combien de km parcourez-vous par an en avion ?\n",
            "TGV": "Combien de km parcourez-vous par an en TGV ?\n",
            "voiture": "Combien de km parcourez-vous en voiture chaque semaine ?\n",
            "motorisation": "Quelle motorisation avez-vous (écrire : électrique ou essence) ?\n",
            "Métro": "Combien de km par semaine prenez-vous le métro ?\n",
            "RER": "Combien de km par semaine prenez-vous le RER ?\n",
            "Bus": "Combien de km par semaine prenez-vous le bus?\n",
        },
        "energie": {
            "Gaz": "Quantité annuelle de Gaz consommé chez vous ?\n",
            "Electricité": "Quantité annuelle d'électricité consommée chez vous ?\n"
        },
        "alimentation": {
            "Repas": "Combien de repas végétariens par semaine ?\n",
            "viande": "Combien de repas avec de la viande bovine par semaine ?\n"
        }
    }

    total_emissions = 0
    detailed_emissions = {}

    for category in questions:
        print(f"\n\nCatégorie : {category}")
        for sub_category in questions[category]:
            if sub_category == 'motorisation':
                motorisation = get_text_input(questions[category][sub_category], valid_responses=['électrique', 'essence'])
                if motorisation == 'electrique':
                    filter_result = base_sample[(base_sample['Nom base français'] == 'Voiture') &
                                                (base_sample['Nom attribut français'].str.contains('électrique', case=False))]
                elif motorisation == 'essence':
                    filter_result = base_sample[(base_sample['Nom base français'] == 'Voiture particulière') &
                                                (base_sample['Nom attribut français'].str.contains('essence', case=False))]
                if filter_result.empty:
                    print("Aucune donnée d'émission trouvée pour cette motorisation.")
                    continue

                emission_factor = filter_result['Total poste non décomposé'].values[0]
                km_per_week = get_numeric_input("Combien de km parcourez-vous en voiture chaque semaine ?\n")
                answer = km_per_week * 52  # Convert weekly to annual
                emissions = answer * emission_factor
                sub_category = f"voiture_{motorisation}"
            else:
                answer = get_numeric_input(questions[category][sub_category])
                if sub_category in ['Voiture particulière', 'Métro', 'RER', 'Bus']:
                    answer = answer * 52  # Convert weekly to annual
                filter_result = base_sample[(base_sample['Nom base français'].str.contains(sub_category, case=False))]

                emission_factor = filter_result['Total poste non décomposé'].values[0]
                emissions = answer * emission_factor

            total_emissions += emissions
            detailed_emissions[sub_category] = emissions

    print("\nBilan des émissions annuelles:")
    for sub_category, emissions in detailed_emissions.items():
        print(f"{sub_category}: {emissions:.2f} kg de CO2")

    print(f"\nTotal annuel: {total_emissions:.2f} kg de CO2")

    category_emissions = {
        "transport": 0,
        "energie": 0,
        "alimentation": 0
    }

    for sub_category, emissions in detailed_emissions.items():
        if sub_category in questions["transport"]:
            category_emissions["transport"] += emissions
        elif sub_category in questions["energie"]:
            category_emissions["energie"] += emissions
        elif sub_category in questions["alimentation"]:
            category_emissions["alimentation"] += emissions

    print("\nBilan des émissions annuelles par grande catégorie:")
    for category, emissions in category_emissions.items():
        print(f"{category}: {emissions:.2f} kg de CO2")

    return detailed_emissions, category_emissions

    # Visualisation
    #visualize_emissions(detailed_emissions)

def visualize_emissions(detailed_emissions):
    ''' 
    Retourne un barplot de l'empreinte carbone par categorie
    '''
    categories = list(detailed_emissions.keys())
    emissions = list(detailed_emissions.values())

    plt.figure(figsize=(12, 8))
    ax = sns.barplot(x=categories, y=emissions, palette="viridis")

    plt.xlabel('Catégories')
    plt.ylabel('Émissions (kg de CO2)')
    plt.title('Bilan des émissions annuelles par catégorie')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Ajouter des étiquettes au-dessus des barres
    for i, value in enumerate(emissions):
        ax.text(i, value + 0.05, f'{value:.2f}', ha='center')
    plt.savefig('Barplot empreinte carbone')
    plt.show()
