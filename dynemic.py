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
    '''weights = [2, 4, 1, 5, 3]
    values = [6, 10, 5, 31, 100]

    capacity = 5'''


    values = [
        # fmt:off
    360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147,
    78, 256, 63, 17, 120, 164, 432, 35, 92, 110, 22, 42, 50, 323, 514, 28,
    87, 73, 78, 15, 26, 78, 210, 36, 85, 189, 274, 43, 33, 10, 19, 389, 276,
    312
        # fmt:on
    ]
    weights = [7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3, 8, 15, 42, 9, 0,
    42, 47, 52, 32, 26, 48, 55, 6, 29, 84, 2, 4, 18, 56, 7, 29, 93, 44, 71,
    3, 86, 66, 31, 65, 0, 79, 20, 65, 52, 13]
        # fmt: on
    
    capacity = 850

    st = time.time()

    max_value, included_items = knapsack(weights, values, capacity)

    et = time.time()

    # Print the results
    print('Max value:', max_value)
    print('Included items:', included_items)

    print('Time taken:', et - st)