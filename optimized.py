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


def knapsack(list_actions, budget_input):
    # Create all needed variables from list
    price = []
    profit = []
    number_actions = len(list_actions)
    budget = budget_input

    for action in list_actions:
        price.append(int(action[1]))
        profit.append(int(action[3]))
    
    # Knapsack problem from https://www.analyticsvidhya.com/blog/2022/05/knapsack-problem-in-python/#:~:text=What%20is%20Python's%20Knapsack%20Problem,a%20specific%20weight%20and%20value
    K = [[0 for x in range(budget + 1)] for x in range(number_actions + 1)]
    for i in range(number_actions + 1):
        for w in range(budget + 1):
            if i == 0  or  w == 0:
                K[i][w] = 0
            elif price[i-1] <= w:
                K[i][w] = max(profit[i-1] + K[i-1][w-price[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[number_actions][budget]
    
print(knapsack(actions_and_profits, 500))


# def knapSack(W, wt, val, n):
#  K = [[0 fоr x in rаnge(W + 1)] fоr x in rаnge(n + 1)]
#  # Build tаble K[][] in bоttоm uр mаnner
#      for i in range(n + 1):
#          for w in range(W + 1):
#              if i == 0  or  w == 0:
#                  K[i][w] = 0
#              elif wt[i-1] <= w:
#                  K[i][w] = max(val[i-1]
#                            + K[i-1][w-wt[i-1]],
#                                K[i-1][w])
#              else:
#                  K[i][w] = K[i-1][w]
#      return K[n][W]

#  # Driver code
#  val = [60, 100, 120]
#  wt = [10, 20, 30]
#  W = 50
#  n = len(val)
#  print(knapSack(W, wt, val, n))
