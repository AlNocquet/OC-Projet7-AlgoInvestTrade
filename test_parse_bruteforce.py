import sys



project_root = r"C:\Users\franc\openclassrooms\projet_7\OC-Projet7-AlgoInvestTrade"
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from bruteforce import get_stocks_from_csv

csv_path = r"C:\Users\franc\openclassrooms\projet_7\OC-Projet7-AlgoInvestTrade\datas\20_stocks.csv"


if __name__ == "__main__":
    try:
        stocks = get_stocks_from_csv(csv_path)
    except FileNotFoundError:
        print("[ERROR] Fichier introuvable -- vérifie le chemin :", csv_path)
        sys.exit(1)
    except Exception as e:
        print("[ERROR] Exception levée lors du parsing :", type(e).__name__, e)
        sys.exit(1)

    print(f"\nNombre d'actions parsées : {len(stocks)}\n")
    for i, s in enumerate(stocks[:10], start=1):
        # s est un tuple (name, price, profit)
        print(f"{i:02d}: name={s[0]!r}, price={s[1]:.2f}, profit={s[2]:.2f}")

    print("\n--- Fin du test ---\n")