from ortools.algorithms.python import knapsack_solver
import random
import pandas as pd
import time

def main():
    # Create the solver.
    solver = knapsack_solver.KnapsackSolver(
        knapsack_solver.SolverType.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,
        "KnapsackExample",
    )

    # read the values from csv file
    df = pd.read_csv("random_data.csv")
    weights = df["weights"].tolist()
    values = df["values"].tolist()
    capacities = [random.randint(1, 5_000)]



    st = time.time()

    solver.init(values, weights, capacities)
    computed_value = solver.solve()

    packed_items = []
    packed_weights = []
    total_weight = 0
    print("Total value =", computed_value)
    for i in range(len(values)):
        if solver.best_solution_contains(i):
            packed_items.append(i)
            packed_weights.append(weights[0][i])
            total_weight += weights[0][i]
    et = time.time()
    #print("Total weight:", total_weight)
    #print("Packed items:", packed_items)
    #print("Packed_weights:", packed_weights)
    print('Time taken:', et - st)


if __name__ == "__main__":
    main()