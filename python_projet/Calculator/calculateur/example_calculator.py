import pandas as pd

def calculate():
    """
    CECI EST UN EXEMPLE, A MODIFIER
    """
    questions = {
        "transport": {
            "avion": "Combien de km avez-vous parcouru en 1 an en avion ?\n",
            "TVG": "Idem en TVG ?\n",
            "voiture": "Combien de km parcourez-vous en voiture chaque semaine ?\n",
            "motorisation": "Quelle motorisation avez-vous (écrire : electrique, essence ou diesel) ?\n",
            "Métro": "Combien de fois par semaine prenez-vous le métro ?\n",
            "RER": "Idem pour le RER ?\n",
        },
        "energie": {
            "type": "quel type d'énergie utilisez-vous chez vous (écrire : fioul, gaz, granules, electricite) ?\n",
            "qty": "quantite annuelle ?"
        },
        "alimentation": "Combien de repas végératiens par semaine ?\n"
    }

    for ty in questions:
        print(f"\n\nCatégorie : {ty}")
        if isinstance(questions.get(ty), dict):
            for subty in questions.get(ty):
                input(questions.get(ty).get(subty))
        else:
            input(questions.get(ty))

    print("\n\n")
    print("CE PROGRAMME EST UN EXEMPLE, LES VALEURS SONT ARBITRAIRES")
    print("\n\n")
    print("Votre empreinte carbone annuelle est de 9.8 tonnes")
    print("Pas mal, votre êtes dans la moyenne des français. Vous pouvez mieux faire")

    print("\n\nDétails")
    print("Transport : 2.6 t, dont 2 t en voiture et 600 kg en avion")
    print("Alimentation : 2.3 t")
    print("Energie : 2 t")
    print("Autres : 1 t")

if __name__ == "__main__":
    calculate()
