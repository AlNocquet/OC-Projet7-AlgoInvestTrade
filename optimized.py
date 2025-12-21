
import csv
import argparse


def get_stocks_from_csv(csv_path) -> list:
    """
    Read a CSV file and return a list of actions as tuples:
        (name: str, price: float, profit_amount: float)

    Behavior:
    - Skips the header row.
    - Parses price and profit percentage as floats.
    - Skips malformed lines.
    - Skips actions with price <= 0.
    - Converts profit percentage into profit amount in euros:
        profit_amount = price * profit_pct / 100
    - If the file is not found, prints an error and returns an empty list.

    Args:
        csv_path (str): Path to the CSV file.

    Returns:
        list: List of tuples (name, price, profit_amount). May be empty.
    """

    stocks = []

    try:
        with open(csv_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # skip header

            for row in reader:
                try:
                    name = row[0]
                    price = float(row[1])
                    profit_pct = float(row[2])

                    if price <= 0:
                        continue

                    # profit en euros après 2 ans
                    profit_amount = price * profit_pct / 100

                    stocks.append((name, price, profit_amount))

                except (ValueError, IndexError):
                    # ligne mal formée → ignorée
                    continue

    except FileNotFoundError:
        print(f"Erreur : fichier introuvable -> {csv_path}")
        return []

    return stocks


def get_best_investment(stocks: list) -> list:
    """
    Compute the best investment portfolio under a 500€ budget using a 0/1 knapsack
    (dynamic programming).

    Input format:
    - stocks is a list of tuples:
        (name: str, price: float, profit_amount: float)

    Core idea:
    - Convert prices to cents to avoid float precision issues.
    - dp[c] stores the best profit_amount achievable with a budget of c cents.
    - keep[c] stores the index of the last stock used to reach dp[c], allowing
    reconstruction of the final portfolio.

    Constraints:
    - Budget must not exceed 500€.
    - Each stock can be chosen at most once (0/1 behavior).

    Args:
        stocks (list): List of tuples (name, price, profit_amount).

    Returns:
        list: The selected portfolio as a list of tuples (name, price, profit_amount).
    """

    if not stocks:
        return []

    max_invest = 500.0
    capacity = int(max_invest * 100) # budget en centimes

    # Préparer coûts (centimes) + valeurs
    prices_in_cents = []
    values = []

    for stock in stocks:
        prices_in_cents.append(int(stock[1] * 100))
        values.append(stock[2])  # profit en euros

    # dp[c] = Initialisation meilleure valeur possible avec un budget de c centimes
    dp = [0.0] * (capacity + 1)

    # keep[c] = Initialisation -1 "index du dernier stock utilisé pour atteindre dp[c], sinon -1"
    keep = [-1] * (capacity + 1)

    # Sac à dos 0/1 :
    for i in range(len(stocks)):
        cost = prices_in_cents[i]
        value = values[i]

        if cost > capacity:
            continue

        # Descendre = action utilisée qu'une fois
        for c in range(capacity, -1, -1):
            if c < cost:
                continue

            new_value = dp[c - cost] + value

            if new_value > dp[c]:
                dp[c] = new_value
                keep[c] = i

    # Choix budget (<= 500€) meilleure valeur
    best_c = 0
    best_value = 0.0

    for c in range(capacity + 1):
        if dp[c] > best_value:
            best_value = dp[c]
            best_c = c

    # Remonter le fil d'Ariane > panier final
    best_investment = []
    c = best_c

    while c > 0 and keep[c] != -1:
        i = keep[c]
        best_investment.append(stocks[i])
        c -= prices_in_cents[i]

    best_investment.reverse()
    return best_investment


def display_best_performance(best_investment):
    """
    Display the selected portfolio in a simple and readable way.

    Input format:
    - best_investment is a list of tuples:
        (name: str, price: float, profit_amount: float)

    Behavior:
    - Prints each selected action with its cost and profit in euros.
    - Prints the total invested amount and total profit.

    Args:
        best_investment (list): Selected portfolio returned by get_best_investment().

    Returns:
        None
    """

    if not best_investment:
        print("Aucun investissement optimal trouvé.")
        return

    total_cost = 0.0
    total_profit = 0.0

    print("\nMeilleure stratégie d'investissement :\n")

    for name, price, profit in best_investment:
        total_cost += price
        total_profit += profit
        print(f"- {name} | Coût : {price:.2f} € | Profit : {profit:.2f} €")

    print("\nRésumé :")
    print(f"Budget investi : {total_cost:.2f} €")
    print(f"Profit total après 2 ans : {total_profit:.2f} €")


def main():
    """
    Entry point of the optimized program.

    Behavior:
    - Reads the CSV file path from command line arguments.
    - Loads actions from the CSV.
    - Computes the best investment portfolio using the optimized algorithm.
    - Displays the result.

    Returns:
        None
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file", help="Chemin vers le fichier CSV")
    args = parser.parse_args()

    stocks = get_stocks_from_csv(args.csv_file)
    best_investment = get_best_investment(stocks)
    display_best_performance(best_investment)


if __name__ == "__main__":
    main()