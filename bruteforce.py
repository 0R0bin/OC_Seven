# Librairies
import csv
import time
import itertools as iter

# Variables
actions_and_profits = [] # Liste de toutes les actions
BUDGET = 500

print('Lecture du fichier CSV...\n')
# Get all actions / price / profit / calc(profit), put into a matrix
with open('dataset_csv/actions.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        action = [row[0], int(float(row[1])), int(float(row[2])), (int(float(row[1])) * int(float(row[2])) / 100)]
        actions_and_profits.append(action)
        print(f'{row[0]} coût de {row[1]} avec un rendement de {row[2]} et un profit de {action[3]}')
    print('\n')


print('Début de l\'algorithme BruteForce\n')
started_time = time.time()                                          # On récupère le temps au lancement de l'algorithme
profit = 0                                                          # On initialise les profits à 0
best_stocks = []                                                    # On prépare le retour de l'algorithme (meilleure combinaisons d'actions)

for i in range(len(actions_and_profits)):                           # Pour chaque action
    combinations = iter.combinations(actions_and_profits, i+1)      # Renvoies toutes les combinaisons possible (voir DOC Python itertools)
    for combinaison in combinations:                                # Pour chaque possibilité retournée
        total_price = 0                                             # On initialise le coût à 0
        total_profit = 0                                            # On initialise le profit à 0

        for action in combinaison:                                  # Pour chaque action présente dans la combinaison
            total_price += int(action[1])                           # On additionne le coût de toutes les actions dans la séléction de possibilité

        if total_price <= BUDGET:                                   # Si on ne dépasse pas le budget
            for action in combinaison:                              # Pour chaque action présente dans la combinaison
                total_profit += int(action[3])                      # On ajoute le coût de toutes les actions dans la séléction de possibilité

            if total_profit > profit:                               # Si le profit est supérieur au meilleur des profits
                profit = total_profit                               # On sauvegarde le profit
                best_stocks = combinaison                           # On sauvegarde la combinaison 



print('=======================================================================')
print(f'Algorithme BruteForce terminé en {time.time() - started_time} secondes')
print('=======================================================================\n')
print(f"\nMeilleurs investissements possibles ({len(best_stocks)} stock) :\n")
print('(Col1) Nom |(Col2) Prix |(Col3) Profit')

total_price = 0
total_profit = 0

for stock in best_stocks:
    print(f'- {stock[0]} | {stock[1]} € | +{stock[2]} €')
    total_price += stock[1]
    total_profit += stock[3]

print(f'\nCoût total : {total_price}€')
print(f'Gains : {total_profit}€\n')
