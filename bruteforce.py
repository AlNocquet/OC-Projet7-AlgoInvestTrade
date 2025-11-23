import csv


def get_stocks_from_csv(file) -> list:
    """
    Read a CSV and return a list of actions as tuples:
        (name: str, price: float, profit_amount: float)

    Behavior:
    - Parses price and profit as floats (accepts comma as decimal separator).
    - Skips malformed lines with a warning.
    - Skips actions with price <= 0 with a warning.
    - Raises FileNotFoundError if the file is not found.

    Args:
        file (str): Path to the CSV file.

    Returns:
        list: List of tuples (name, price, profit_amount). May be empty.
    """


    stocks = []

    try:
        with open(file, newline="", encoding="utf-8") as csv_File:
            reader = csv.DictReader(csv_File, delimiter=",")
            for lineno, row in enumerate(reader, start=2):
                # Récupération tolérante du nom (plusieurs variantes possibles)
                name = row.get('name') or row.get('Name') or row.get('nom') or row.get('title') or row.get('action')

                try:
                    # gérer les virgules décimales et espaces
                    price_text = (row.get('price') or '').replace(',', '.').strip()
                    profit_text = (row.get('profit') or '').replace(',', '.').strip()

                    price = float(price_text)
                    profit_pct = float(profit_text)
                except (KeyError, ValueError, TypeError):
                    print(f"[WARN] ligne {lineno} ignorée (format invalide) : {row}")
                    continue

                if price <= 0:
                    print(f"[WARN] action ignorée (prix <= 0) : {name} (prix={price})")
                    continue

                profit_amount = price * (profit_pct / 100.0)
                # Même structure tuple (nom, prix, profit) pour compatibilité avec le reste du code
                stocks.append((str(name), float(price), float(profit_amount)))

    except FileNotFoundError:
        print(f"[ERROR] fichier introuvable : {file}")
        raise

    return stocks


def main():

    default_csv = r"C:\Users\franc\openclassrooms\projet_7\OC-Projet7-AlgoInvestTrade\datas\20_stocks.csv"

    csv_path = default_csv

    # Appel fonction de parsing
    try:
        stocks = get_stocks_from_csv(csv_path)
    except FileNotFoundError:
        print(f"[ERROR] fichier introuvable : {csv_path}")
        return
    except Exception as e:
        print(f"[ERROR] exception pendant le parsing : {type(e).__name__} - {e}")
        return

    # Affichage simple pour vérifier le résultat
    print(f"\nNombre d'actions parsées : {len(stocks)}\n")
    for i, s in enumerate(stocks[:10], start=1):
        # s est un tuple (name, price, profit_amount)
        print(f"{i:02d}: name={s[0]!r}, price={s[1]:.2f}€, profit={s[2]:.2f}€")

    print("\n--- Fin du test ---\n")
    return stocks

if __name__ == '__main__':
    main()






##################################################################################################################""

def get_all_combinations(stocks : list) -> list :
    """ Returns all combinations possibles of stocks """

    # DEBUT

    all_combinations = []
    # Créer une liste de toutes les combinaisons possibles d'actions
    for i in range(1, len(stocks) +1) :
        all_combi = combinations(stocks, i)
    # Pour chaque action de la liste "stocks" de 1 à 20, Achat unique d'une action + rechercher toutes les combinaisons uniques possibles (A,B exclut combinaison B,A)
        for combination in all_combi :
            all_combinations.append(combination)
        # Pour chaque combinaison, l'ajouter à la liste all_combinations 
    #print(len(all_combinations))
    #print(all_combinations)
    return all_combinations
        
    # FIN


def get_best_investment(all_combinations : list) -> list:
    """ Returns the best investment with a basket cost <= €500 """

    # DEBUT

    valid_investments = []

    max_cost = 500

    for combination in all_combinations:
        combination_cost = 0
        combination_profit = 0
        for i in range (len(combination)) :
            combination_cost += combination[i][1]
            combination_profit += combination[i][2]
    # POUR chaque combinaison d'actions de la liste des combinaisons possibles, initialiser le coût et le profit à 0 
        # PUIS additioner le coût et le profit des actions de chaque combinaison avec les index 

        if combination_cost <= max_cost :
        # SI le coût de la combinaison d'actions est inférieur ou égale à 500€
            valid_investments.append((combination, combination_cost, combination_profit))
            #print(len(valid_investments))
    #print(valid_investments[0:5])
    #print(combination_cost)
            # Ajouter la combinaison à la liste des propositions

    sorted_investments = sorted(valid_investments, reverse=True, key=lambda valid_investment : valid_investment[2])
    best_investment = sorted_investments[0]
    print(Fore.GREEN + Style.BRIGHT + f"Le meilleur éventail d'investissements est : " + Style.RESET_ALL)
    for b in best_investment[0] :
        print(" "+ f"{b}")
    print(Fore.GREEN + Style.BRIGHT + f"Avec un coût total de : " + Style.RESET_ALL + f"{round(best_investment[1],2)}")
    print(Fore.GREEN + Style.BRIGHT + f"Avec un profit total de : " + Style.RESET_ALL + f"{round(best_investment[2],2)}")
    
    return best_investment  

    # Trier la liste des proposition valides par ordre décroissant 
    # Printer 1er élément de la liste et ses valeurs

    # FIN

#def main():
    #stocks = get_stocks_from_csv(file="datas/20_stocks.csv")
    #combinations = get_all_combinations(stocks)
    #get_best_investment(combinations)


