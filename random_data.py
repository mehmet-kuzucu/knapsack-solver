#create a random data set
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# create a random data set for knapsack problem
def create_random(N):
    #create a random data set
    #create a random data set
    weights = []
    values = []
    for i in range(1, N):
        weights.append(random.randint(1, N))
        values.append(random.randint(1, N))
    return weights, values

if __name__ == "__main__":
    weights, values = create_random(10_000)
    #save the data set to a csv file
    df = pd.DataFrame({'weights': weights, 'values': values})
    df.to_csv('random_data.csv', index=False)
    print('Done!')