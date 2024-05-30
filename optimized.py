
import csv
import argparse
from colorama import Fore, Style, Back


def get_stocks_from_csv(file) -> list:
    """ Gets a list of stocks from the csv file and excludes irrelevant datas (profits <= 0)"""

    stocks = []

    with open(file, newline="") as csv_File:
        reader = csv.DictReader(csv_File, delimiter=",")
        for row in reader:
            stock = (row['name'], float(row['price']), float(row['profit']))
            if stock[1] > 0 :
                stocks.append(stock)
    return stocks


def get_best_investment(stocks: list) -> list:
    """ Sorts stocks by performance and buy up to a total purchase cost of €500 """

    best_investment = []

    max_invest = 500

    stocks_by_profit = sorted(stocks, reverse=True, key=lambda stocks : stocks[2])

    for stock in stocks_by_profit:
        cost_stock = stock[1]
        if cost_stock <= max_invest:
            max_invest -= cost_stock
            # if max = 0 :
            # break
            best_investment.append(stock)

    return best_investment

def display_best_performance(best_investment): 
    """ Displays results """
    
    total_cost = 0
    total_profit = 0
    total_value = 0

    print(Fore.GREEN + Style.BRIGHT +"\n"+ f"Le meilleur éventail d'investissements pour 500€ d'achat est : " + "\n" + Style.RESET_ALL)

    for b_i in best_investment :
        print(" "+ f"{b_i}")
        total_cost += b_i[1]
        cost_stock = b_i[1]
        perf_stock = b_i[2] /100
        profit_stock = cost_stock * perf_stock
        total_profit += profit_stock
        new_value = cost_stock + profit_stock
        total_value += new_value

    print(Fore.GREEN + Style.BRIGHT + "\n" + f"Avec un investissement de départ (coût total) de : " + Style.RESET_ALL + f"{round(total_cost,2)}€")

    print(Fore.GREEN + Style.BRIGHT + f"Un profit NET total après 2 ans de : " + Style.RESET_ALL + f"{round(total_profit,2)}€")

    print(Fore.GREEN + Style.BRIGHT + f"Avec valeur de rachat après 2 ans de : " + Style.RESET_ALL + f"{round(total_value,2)}€")


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Nom du ficher à analyser (avec chemin éventuel). ex : data\\dataset1.csv")
    args = parser.parse_args()
    file_name = args.file
    print(file_name)
    
    stocks = get_stocks_from_csv(file_name)
    best_investment = get_best_investment(stocks)
    display_best_performance(best_investment)


if __name__ == '__main__':
    start = main()