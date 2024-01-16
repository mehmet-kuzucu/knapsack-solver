import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time


def knapsack(weights, values, capacity):
    n = len(weights)
    
    # Create a 2D table to store solutions to subproblems
    dp = []
    for _ in range(n + 1):
        row = [0] * (capacity + 1)
        dp.append(row)



    # Build the table in a bottom-up manner
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                # Decide whether to include the current item or not
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                # If the current item is too heavy, exclude it
                dp[i][w] = dp[i - 1][w]


    # The bottom-right cell contains the maximum value
    max_value = dp[n][capacity]
    

    # Find the items included in the knapsack
    included_items = []
    w, i = capacity, n
    while w > 0 and i > 0:
        if dp[i][w] != dp[i - 1][w]:
            included_items.append(i - 1)
            w -= weights[i - 1]
        i -= 1

    included_items.reverse()

    return max_value, included_items


if __name__ == "__main__":
    '''
    # Read the data set
    df = pd.read_csv('random_data.csv')
    weights = df['weights'].tolist()
    values = df['values'].tolist()
    capacity = random.randint(1, 5_000)


    # print the size of the data set in terms of mega bytes
    print('Size of the data set:', df.memory_usage().sum() / 1024 ** 2, 'MB')
'''

    # Solve the knapsack problem
    weights = [2, 4, 1, 5]
    values = [6, 10, 5, 31]
    capacity = 3

    st = time.time()

    max_value, included_items = knapsack(weights, values, capacity)

    et = time.time()

    # Print the results
    print('Max value:', max_value)
    print('Included items:', included_items)

    print('Time taken:', et - st)










