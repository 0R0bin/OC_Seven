# Librairies
import csv
import time
# import controllers as c
# import views as v


# Variables
DEFAULT_BUDGET = 500

def main():
    # budget = v.ask_budget(DEFAULT_BUDGET)
    # filename = v.ask_dset()
    # stock_list = c.process_csv(filename)
    # v.csv_ok()
    # start_time = time.time()
    # knapsack_result = c.knapsack(stock_list, budget)
    # v.report(knapsack_result, time.time(), start_time)
    budget = ask_budget(DEFAULT_BUDGET)
    filename = ask_dset()
    stock_list = process_csv(filename)
    csv_ok()
    start_time = time.time()
    knapsack_result = knapsack(stock_list, budget)
    report(knapsack_result, time.time(), start_time)

main()



# VIEWS
def ask_budget(default_budget):
    """
    Ask user input to chose budget
    """
    print('Souhaitez-vous utiliser un budget personnalisé ?')
    b_choice = input('Répondre par (y / oui / yes) pour le personnaliser ou autre pour garder 500€ : ')

    if b_choice.lower() in ['y', 'yes', 'oui']:
        budget = input('Merci d\'entrer le budget : ')
        # Vérification du budget en INT
        try:
            budget = int(budget)
        except ValueError:
            print('Merci d\'indiquer votre budget au format INT\n')
            return ask_budget(default_budget)
        print(f'\nBudget de {budget}€ choisi\n')
        return int(budget)

    print('\nBudget par défaut choisi (500€)')
    return default_budget


def ask_dset():
    """
    Demander à l'utilisateur de choisir un jeu de données
    """
    print('\nMerci de choisir un jeu de données et de rentrer son nom sans extension et sans tenir compte du dossier')
    print('Exemple d\'input possible :\n - actions \n - dataset1')
    dset_choice = input('Nom du jeu de données : ')

    filename = f'dataset_csv/{dset_choice}.csv'

    print(f'\nFichier choisi : {filename}')
    b_continue = input('Confirmez-vous ce choix ? (y ou n) ')

    if b_continue.lower() in ['y', 'yes', 'oui']:
        try:
            with open(filename, 'r'):
                print('\nChoix validé, lecture du fichier en cours\n')
                return filename
        except FileNotFoundError:
            print(f"Erreur : Le fichier '{filename}' n'existe pas")
            return ask_dset()

    return ask_dset()


def csv_ok():
    """Print CSV OK, launch knapsack"""
    return '\nRécupération des données du fichier terminé, lancement de l\'algorithme...'


def report(best_stock, actual_time, started_time):
    """
    Affichage algo terminé avec :
     - Temps passé
     - Coût
     - Gains
    """
    print('======================================================================')
    print(f'Algorithme Knapsack terminé en {actual_time - started_time} secondes')
    print('======================================================================\n')
    print(f"\nMeilleurs investissements possibles ({len(best_stock)} stock) :\n")
    print('(Col1) Nom |(Col2) Prix |(Col3) Profit')

    total_price = 0
    total_profit = 0

    for stock in best_stock:
        print(f'- {stock[0]} | {stock[1]} € | +{stock[2]} €')
        total_price += stock[1]
        total_profit += stock[3]

    print(f'\nCoût total : {total_price / 100}€')
    print(f'Gains : {total_profit}€\n')


def process_csv(filename):
    """
    Traitement du fichier CSV avec suppression des lignes où le coût ou le rendement sont à 0
    Renvoies une liste avec Nom / Coût / Profit / Rendement
    """
    with open(filename) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')

        all_info_stock_list = []

        for row in csv_reader:
            try:
                # Suppression des lignes à 0 en coût ou rendement
                if float(row[1]) <= 0 or float(row[2]) <= 0:
                    pass
                else:
                    stock = [row[0], int(float(row[1]) * 100), float(row[2]), float(row[1]) * (float(row[2]) / 100)]
                    all_info_stock_list.append(stock)
            except ValueError:
                print(f'Erreur de format sur la ligne {row}')
                print('Fichier en cours de lecture...\n')
                continue

        return all_info_stock_list

# CONTROLLERS

def knapsack(stock_list, budget):
    """Algorithme knapsack
    Source : https://www.geeksforgeeks.org/python-program-for-dynamic-programming-set-10-0-1-knapsack-problem/
    Retourne la meilleur combinaison d'actions
    """
    budget = budget * 100
    len_stock_list = len(stock_list)
    price = []
    profit = []

    for stock in stock_list:
        price.append(stock[1])
        profit.append(stock[3])

    # Recherche knapsack
    K = [[0 for w in range(budget + 1)] for i in range(len_stock_list + 1)]

    for i in range(len_stock_list + 1):
        for w in range(1, budget + 1):
            if price[i-1] <= w:
                K[i][w] = max(profit[i-1] + K[i-1][w-price[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    # Retrieve combination of shares from optimal profit
    best_stocks = []

    while budget >= 0 and len_stock_list >= 0:

        if K[len_stock_list][budget] == \
                K[len_stock_list-1][budget - price[len_stock_list-1]] + profit[len_stock_list-1]:

            best_stocks.append(stock_list[len_stock_list-1])
            budget -= price[len_stock_list-1]

        len_stock_list -= 1

    return best_stocks
