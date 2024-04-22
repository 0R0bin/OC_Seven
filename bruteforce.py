# Librairies
import csv
# Utiliser panda pour ouvrir les csv

# Variables
actions_and_profits = []
budget = 500

# Get all actions / price / profit into a matrix
with open('dataset_csv/actions.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        action = [row[0], row[1], row[2]]
        actions_and_profits.append(action)
        print(f'{row[0]} coût de {row[1]} avec un rendement de {row[2]}.\n')

# Determination of each profit, save it into our matrix
for action in actions_and_profits:
    action.append((int(action[2]) / 100) * int(action[1]))

i = 0
while budget > 0:
    budget -= int(actions_and_profits[i][1])
    # if budget < 0:
    #     budget += int(actions_and_profits[i][1])
    i += 1
    print(budget)
