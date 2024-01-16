class Node:
    def __init__(self, level, value, weight, bound, path):
        self.level = level  # The level of the node in the search tree
        self.value = value  # The value of the node's solution
        self.weight = weight  # The weight of the node's solution
        self.bound = bound  # The upper bound of the node
        self.path = path  # The path taken to reach this node

def knapsack_branch_and_bound(weights, values, capacity):
    n = len(weights)

    # Sort items based on value-to-weight ratio (greedy step)
    value_per_weight = [(values[i] / weights[i], i) for i in range(n)]
    value_per_weight.sort(reverse=True)

    print(value_per_weight)

    # Initialize the root node
    root = Node(level=-1, value=0, weight=0, bound=0, path=[])

    # Initialize priority queue (min heap) for nodes
    priority_queue = [root]

    max_value = 0  # Initialize maximum value

    i = 0

    while priority_queue:
        # Get the next node from the priority queue
        current_node = priority_queue.pop(0)

        # If the current node's level is the last level, update the maximum value
        if current_node.level == n - 1:
            max_value = max(max_value, current_node.value)
            continue

        # Check if the current item can be included
        if current_node.weight + weights[value_per_weight[current_node.level + 1][1]] <= capacity:
            # Include the item
            include_index = value_per_weight[current_node.level + 1][1]
            include_node = Node(
                level=current_node.level + 1,
                value=current_node.value + values[include_index],
                weight=current_node.weight + weights[include_index],
                bound=current_node.bound,
                path=current_node.path + [include_index],
            )
            if include_node.value > max_value:
                max_value = include_node.value
            priority_queue.append(include_node)

        # Exclude the current item
        exclude_node = Node(
            level=current_node.level + 1,
            value=current_node.value,
            weight=current_node.weight,
            bound=current_node.bound,
            path=current_node.path,
        )

        # Calculate the upper bound for the excluded node
        exclude_node.bound = calculate_bound(exclude_node, n, weights, values, capacity, value_per_weight)

        # If the upper bound is greater than the current max_value, add to the queue
        if exclude_node.bound > max_value:
            priority_queue.append(exclude_node)

        # Sort the priority queue based on the bound (greedy step)
        priority_queue.sort(key=lambda x: x.bound, reverse=True)

    return max_value

def calculate_bound(node, n, weights, values, capacity, value_per_weight):
    # If the weight exceeds the capacity, the node is infeasible
    if node.weight >= capacity:
        return 0

    # Include the remaining items using their full weight until the capacity is reached
    bound = node.value
    remaining_capacity = capacity - node.weight
    j = node.level + 1

    while j < n and weights[value_per_weight[j][1]] <= remaining_capacity:
        bound += values[value_per_weight[j][1]]
        remaining_capacity -= weights[value_per_weight[j][1]]
        j += 1

    # If there are more items left, include a fraction of the next item
    if j < n:
        bound += (remaining_capacity / weights[value_per_weight[j][1]]) * values[value_per_weight[j][1]]

    return bound

# Example usage:

weights = [3, 5, 1, 2, 4]
values = [100, 31, 6, 6, 10]
capacity = 5
max_value = knapsack_branch_and_bound(weights, values, capacity)
print(f"Maximum value using Branch and Bound: {max_value}")
