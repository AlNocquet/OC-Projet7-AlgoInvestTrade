
import csv
from itertools import combinations
from colorama import Fore, Style


# PSEUDO CODE BRUTEFORCE

# DEBUT 

    # VARIABLE EXTRAIRE 20 ACTIONS DANS CSV
    # VARIABLE CALCULER TOUTES LES COMBINAISONS POSSIBLES
    # VARIABLE COUT TOTAL et PROFIT DE CHAQUE COMBINAISON
    # VARIABLE MEILLEURE PERFORMANCE (CONDITION < 500 €)

# FIN


def get_stocks_from_csv(file) -> list:
    """Gets a list of stocks from the csv file "20_stocks.csv" """

    # DEBUT

    stocks = []
    with open(file, newline="") as csv_File:
        reader = csv.DictReader(csv_File, delimiter=",")
    # Sélectionner le fichier CSV et le parcourir
        for row in reader:
            stock = (str(row['name']), int(row['price']), ((int(row['profit']) * 0.01) * int(row['price'])))
        # POUR chaque ligne du fichier CSV, définir une action comme suit :
            # name : "chaîne de caractère" <- row 0 ;
            # cost : INT (ENTIER) <- row 1 ;
            # Profit : INT (ENTIER / PERCENT) <- row 2 (Convertir % en Int avec le prix row[1]) ;
            stocks.append(stock)
            # Ajouter à la liste d'actions
    #print(stocks)
    return stocks

    # FIN


def get_all_combinations(stocks : list) -> list :
    """ Returns all combinations possibles of stocks """

    # DEBUT

    all_combinations = []
    # Créer une liste de toutes les combinaisons possibles d'actions
    for i in range(1, len(stocks) +1) :
        all_combi = combinations(stocks, i)
    # Pour chaque action de la liste "stocks" de 1 à 20, rechercher toutes les combinaisons uniques possibles (exclure doublon + valeur multiplié par elle-même)
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
    # POUR chaque combinaison d'actions de la liste des combinaisons possibles, initialiser à 0 le coût et le profit 
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

def main():
    stocks = get_stocks_from_csv(file="datas/20_stocks.csv")
    combinations = get_all_combinations(stocks)
    get_best_investment(combinations)

if __name__ == '__main__':
    start = main()