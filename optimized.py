import time
import controllers as c
import views as v


# Variables
DEFAULT_BUDGET = 500


def main():
    budget = v.ask_budget(DEFAULT_BUDGET)
    filename = v.ask_dset()
    stock_list = c.process_csv(filename)
    v.csv_ok()
    start_time = time.time()
    knapsack_result = c.knapsack(stock_list, budget)
    v.report(knapsack_result, time.time(), start_time)

main()
