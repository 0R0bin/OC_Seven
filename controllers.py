import csv

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
    # Construction du tableau K avec des dimensions (len_stock_list + 1) x (budget + 1)
    K = [[0 for w in range(budget + 1)] for i in range(len_stock_list + 1)]

    # Itération sur chaque ligne du tableau K (représentant chaque élément de la liste des stocks)
    for i in range(len_stock_list + 1):
        # Itération sur chaque colonne du tableau K (représentant chaque poids de budget possible)
        for w in range(1, budget + 1):
            # Si le prix de l'élément actuel (i-1) est inférieur ou égal au poids de budget actuel (w)
            if price[i-1] <= w:
                # Récupération valeur max entre :
                K[i][w] = max(
                    # Profit obtenu en incluant l'élément actuel
                    profit[i-1] + K[i-1][w-price[i-1]],
                    # Valeur maximale du profit en excluant l'élément actuel
                    K[i-1][w])
            else:
                # Si le prix de l'élément est supérieur au poids de budget actuel
                K[i][w] = K[i-1][w]

    # Retrieve combination of shares from optimal profit
    best_stocks = []

    # Boucle tant que le budget ou tous les stocks ne sont pas épuisés
    while budget >= 0 and len_stock_list >= 0:

        # On vérifie si le prix change en ajoutant l'élément actuel
        if K[len_stock_list][budget] == K[len_stock_list-1][budget - price[len_stock_list-1]] + profit[len_stock_list-1]:
            best_stocks.append(stock_list[len_stock_list-1]) # S'il change, on ajoute l'action
            budget -= price[len_stock_list-1] # Et on décrémente le budget

        # Passer à l'action précédente pour l'itération suivante
        # Car on déconstruit le tableau
        len_stock_list -= 1

    return best_stocks
