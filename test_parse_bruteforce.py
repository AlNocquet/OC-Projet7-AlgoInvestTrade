from bruteforce import get_stocks_from_csv


csv_path = "datas/20_stocks.csv"


if __name__ == "__main__":

    stocks = get_stocks_from_csv(csv_path)

    print("Nombre d'actions lues :", len(stocks))
    print("Voici les premières actions :\n")

    for i, s in enumerate(stocks[:10], start=1):
        name = s[0]
        price = s[1]
        profit = s[2]
        print(i, ":", "name =", name, ", price =", price, ", profit =", profit)

    print("\n--- Fin du test ---")