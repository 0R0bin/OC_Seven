# Librairies
import csv

# Variables
actions_and_profits = []
budget = 500

# Get all actions / price / profit into a matrix
with open('actions.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        action = [row[0], row[1], row[2]]
        actions_and_profits.append(action)
        print(f'{row[0]} coût de {row[1]} avec un rendement de {row[2]}.\n')

# Determination of each profit, save it into our matrix
for action in actions_and_profits:
    action.append((int(action[2]) / 100) * int(action[1]))


def printknapSack(list_actions, budget_input):

    # Create all needed variables from list
    price = []
    profit = []
    number_actions = len(list_actions)
    budget = budget_input

    for action in list_actions:
        price.append(int(action[1]))
        profit.append(int(action[3]))


    K = [[0 for w in range(budget + 1)] for i in range(number_actions + 1)]
             
    for i in range(number_actions + 1):
        for w in range(budget + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif price[i - 1] <= w:
                K[i][w] = max(profit[i - 1] + K[i - 1][w - price[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
 
    # stores the result of Knapsack
    res = K[number_actions][budget]
    print(res)
     
    w = budget
    for i in range(number_actions, 0, -1):
        if res <= 0:
            break
        if res == K[i - 1][w]:
            continue
        else:
            print(price[i - 1])
             
            res = res - profit[i - 1]
            w = w - price[i - 1]
 
     
printknapSack(actions_and_profits, 500)