import csv
from itertools import combinations


def get_stocks_from_csv(csv_path) -> list:
    """
    Read a CSV and return a list of actions as tuples:
        (name: str, price: float, profit_amount: float)

    Behavior:
    - Parses price and profit as floats (accepts comma as decimal separator).
    - Skips malformed lines with a warning.
    - Skips actions with price <= 0 with a warning.
    - Raises FileNotFoundError if the file is not found.

    Args:
        csv_path (str): Path to the CSV file.

    Returns:
        list: List of tuples (name, price, profit_amount). May be empty.
    """

    stocks = []

    try:
        with open(csv_path, newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=",")
            for line_number, row_dict in enumerate(reader, start=2):
                # tolerant name lookup (several possible header names)
                name = row_dict.get('name') or row_dict.get('Name') or row_dict.get('nom') \
                       or row_dict.get('title') or row_dict.get('action')

                try:
                    # handle comma decimal and surrounding spaces
                    price_text = (row_dict.get('price') or '').replace(',', '.').strip()
                    profit_text = (row_dict.get('profit') or '').replace(',', '.').strip()

                    # row_dict.get('price') or '': retrieve the string for the price column, or '' if it is missing
                    # .replace(',', '.') : replace a comma with a period to accept decimals written like 12,5
                    # .strip() : remove extra spaces at the beginning/end

                    # convert to numbers
                    price = float(price_text)
                    profit_pct = float(profit_text)

                except (KeyError, ValueError, TypeError):
                    print(f"[WARN] line {line_number} ignored (invalid format): {row_dict}")
                    continue

                if price <= 0:
                    print(f"[WARN] action ignored (price <= 0): {name} (price={price})")
                    continue

                profit_amount = price * (profit_pct / 100.0)
                # keep tuple structure (name, price, profit) for compatibility
                stocks.append((str(name), float(price), float(profit_amount)))

    except FileNotFoundError:
        print(f"[ERROR] file not found: {csv_path}")
        raise

    return stocks


def iter_combinations(stocks):
    """
    Yield all non-empty combinations of items from `stocks`.

    Behavior:
    - Produces combinations of size 1..len(stocks) in increasing size order.
    - Yields each combination as a tuple and does not build a full list in memory.
    - If `stocks` is empty, yields nothing.

    Args:
        stocks (sequence): Sequence of items (e.g. tuples (name, price, profit)).

    Returns:
        generator: Yields tuples representing each combination.
    """

    # count how many stock items are available (used to know the maximum combination size)
    num_stocks = len(stocks)
    
    # loop over desired combination sizes: 1, then 2, ..., up to all items
    # (this ensures we produce ('A',) ('B',) ('C',) before ('A','B'), etc.)
    for combo_size in range(1, num_stocks + 1):

        # for the current combo_size, generate each tuple of that length from `stocks`
        for combo in combinations(stocks, combo_size):

            # yield hands this combination to the caller and pauses until the caller requests the next one
            yield combo



def get_best_investment_bruteforce(stocks, max_cost=500.0):
    """
    Brute-force simple : parcourt toutes les combinaisons et renvoie :
      {'stocks': combo_tuple, 'total_cost': float, 'total_profit': float}
    ou None si aucune combinaison valide.
    """
    best = None
    for combo in iter_combinations(stocks):
        total_cost = sum(item[1] for item in combo)
        if total_cost > max_cost:
            continue
        total_profit = sum(item[2] for item in combo)
        if best is None or total_profit > best['total_profit']:
            best = {'stocks': combo, 'total_cost': total_cost, 'total_profit': total_profit}

    return best


def display_best_investment(best):
    """Affiche le meilleur portefeuille trouvé par l'algorithme brute force."""

    if best is None:
        print("Aucune combinaison ne respecte la contrainte de budget.")
        return

    # Récupération des données
    combo = best['stocks']
    total_cost = best['total_cost']
    total_profit = best['total_profit']
    total_value = total_cost + total_profit

    print("\nMeilleure combinaison d'actions trouvée :\n")

    # Afficher chaque action une par une
    for stock in combo:
        name = stock[0]
        price = stock[1]
        profit = stock[2]
        print("- Action :", name, "| coût :", price, "€ | profit :", profit, "€")

    print("\nRécapitulatif :")
    print("Coût total du portefeuille :", total_cost, "€")
    print("Profit total après 2 ans   :", total_profit, "€")
    print("Valeur de revente totale   :", total_value, "€")


def main():

    csv_path = "datas/20_stocks.csv"

    try:
        stocks = get_stocks_from_csv(csv_path)

    except FileNotFoundError:
        print("[ERREUR] Fichier introuvable :", csv_path)
        return

    except Exception as e:
        print("[ERREUR] Problème pendant la lecture du fichier :", e)
        return

    print("\nNombre d'actions lues :", len(stocks))

    print("Voici les premières actions :\n")

    for i, s in enumerate(stocks[:10], start=1):
        name = s[0]
        price = s[1]
        profit = s[2]
        print(i, ":", "name =", name, ", price =", price, "€ , profit =", profit, "€")

    best = get_best_investment_bruteforce(stocks, max_cost=500.0)

    display_best_investment(best)

    print("\n--- Fin du programme bruteforce ---\n")