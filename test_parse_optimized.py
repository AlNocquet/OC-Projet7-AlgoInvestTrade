from optimized import get_stocks_from_csv, get_best_investment

csv_path = "datas/dataset1_Python+P7.csv"

if __name__ == "__main__":

    stocks = get_stocks_from_csv(csv_path)

    print("Nombre d'actions lues :", len(stocks))
    print("Premières actions :\n")

    for i, s in enumerate(stocks[:10], start=1):
        name, price, profit = s
        print(f"{i}: name={name}, price={price}€, profit={profit}€")

    best = get_best_investment(stocks)

    print("\nPortefeuille optimal :\n")
    total_cost = 0
    total_profit = 0

    for name, price, profit in best:
        total_cost += price
        total_profit += profit
        print(f"- {name} | coût={price}€ | profit={profit}€")

    print("\nRésumé :")
    print("Coût total :", total_cost, "€")
    print("Profit total :", total_profit, "€")