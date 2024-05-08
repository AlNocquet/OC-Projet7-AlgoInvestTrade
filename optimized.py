
import csv
from colorama import Fore, Style, Back


# PSEUDO CODE BRUTEFORCE

# DEBUT 

    # VARIABLE INPUT POUR CHOIX CSV
    # VARIABLE MANAGE MAIN MENU
    # VARIABLE TRI FICHIER D'ACTION SELECTIONNÉ PAR MEILLEURS RENDEMENTS
    # VARIABLE ACHETER JUSQUE 500€


# FIN


QUIT_CODE = "Exit"
MAX_COST = 500

class CancelError(Exception):
    pass


def display_main_menu():
    """Diplays MAIN MENU and returns the user's choice - or not if the user enters quit"""

    while True:
        main_menu_settings("MENU PRINCIPAL")
        subtitle_menu_settings("BIENVENU ! Choisissez un fichier pour l'analyser ou Taper *Exit* pour quitter !")

        choice_menu_settings("Tapez 1 : 20_actions.csv")
        choice_menu_settings("Tapez 2 : dataset1_Python+P7.csv")
        choice_menu_settings("Tapez 3 : dataset2_Python+P7.csv")

        choice = get_user_answer(label="Entrez votre choix : ")

        valid_choice = ["1", "2", "3", "exit"]

        if choice in valid_choice:
            return choice

        if choice.lower() == QUIT_CODE:
            display_message("Au revoir !")

        else:
            display_error_message("Choix invalide !")


def manage_main_menu(choice):
    """Manages MAIN MENU and returns the user's choice of CSV file (and convert profit in €) - or not if the user enters quit """

    stocks = []

    while True:
        choice = display_main_menu()

        if choice == QUIT_CODE:
            exit()

        elif choice == "1":
            with open(file="datas/20_stocks.csv", newline="") as csv_File:
                reader = csv.DictReader(csv_File, delimiter=",")
                for row in reader:
                    stock = (str(row['name']), int(row['price']), ((int(row['profit']) * 0.01) * int(row['price'])))
                    stocks.append(stock)

        if choice == "2":
            with open(file="datas/dataset1_Python+P7.csv", newline="") as csv_File:
                reader = csv.DictReader(csv_File, delimiter=",")
                for row in reader:
                    stock = (row['name'], int(float(row['price'])), (int(float(row['price'])) * float(row['profit']) * 0.01))
                    stocks.append(stock)
                
        elif choice == "3":
            with open(file="datas/dataset2_Python+P7.csv", newline="") as csv_File:
                reader = csv.DictReader(csv_File, delimiter=",")
                for row in reader:
                    stock = (row['name'], int(float(row['price'])), (int(float(row['price'])) * float(row['profit']) * 0.01))
                    stocks.append(stock)


        return stocks

def get_best_performances(stocks: list) -> list:
    """ Sorts stocks by performance """

    sorted_stocks = sorted(stocks, reverse=True, key=lambda stocks : stocks[1])
    best_performances = sorted_stocks
    for bp in best_performances :
        print("\n" + " "+ f"{bp}")














def get_user_answer(label):
    """Display field "Enter your choice" and returns the user's response"""

    while True:
        value = input(Fore.WHITE + Style.BRIGHT + f"\n {label}" + Style.RESET_ALL ).lower()
        return value

def display_message(msg: str):
    """Settings messages in app"""  
    print("\n")
    print(Fore.WHITE + Style.BRIGHT + msg)

def display_error_message(msg: str):
    """Settings error messages in app"""
    print("\n" + Fore.RED + Style.BRIGHT + msg)

def display_success_message(msg: str):
    """Settings success messages in app"""
    print("\n" + Fore.GREEN + Style.BRIGHT + msg)

def main_menu_settings(msg: str) -> str:
    """Settings the title of main menu"""
    print("\n")
    print(Fore.GREEN + Style.BRIGHT + msg.center(100) + Style.RESET_ALL)

def subtitle_menu_settings(msg: str) -> str:
    """Settings the subtitle of main menu"""
    print(Fore.WHITE + msg.center(100) + Style.RESET_ALL)
    print("\n")

def choice_menu_settings(msg: str) -> str:
    """Settings the subtitle of main menu"""
    print(Fore.GREEN + msg + Style.RESET_ALL)



def main():

    main_menu =  manage_main_menu(choice=display_main_menu())
    get_best_performances(main_menu)

if __name__ == '__main__':
    start = main()