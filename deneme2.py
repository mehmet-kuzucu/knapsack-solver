import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, level, value, weight, bound, path):
        self.level = level
        self.value = value
        self.weight = weight
        self.bound = bound
        self.path = path

def visualize_knapsack_tree(tree):
    pos = nx.spring_layout(tree, seed=42)
    labels = {node: f"Level: {node.level}\nValue: {node.value}\nWeight: {node.weight}\nBound: {node.bound}" for node in tree.nodes}
    
    colors = ['skyblue' if 'Include' in labels[node] else 'lightcoral' for node in tree.nodes]
    
    nx.draw(tree, pos, labels=labels, with_labels=True, node_size=700, node_color=colors, font_size=8)
    plt.title("Knapsack Branch and Bound Tree")
    plt.show()

def knapsack_branch_and_bound(weights, values, capacity):
    n = len(weights)
    value_per_weight = [(values[i] / weights[i], i) for i in range(n)]
    value_per_weight.sort(reverse=True)
    
    root = Node(level=-1, value=0, weight=0, bound=0, path=[])
    priority_queue = [root]
    
    tree = nx.Graph()
    tree.add_node(root, label="Root")
    
    while priority_queue:
        current_node = priority_queue.pop(0)

        if current_node.level == n - 1:
            continue

        include_index = value_per_weight[current_node.level + 1][1]
        include_node = Node(
            level=current_node.level + 1,
            value=current_node.value + values[include_index],
            weight=current_node.weight + weights[include_index],
            bound=current_node.bound,
            path=current_node.path + [include_index],
        )
        priority_queue.append(include_node)
        tree.add_edge(current_node, include_node, label="Include")
        
        exclude_node = Node(
            level=current_node.level + 1,
            value=current_node.value,
            weight=current_node.weight,
            bound=current_node.bound,
            path=current_node.path,
        )
        exclude_node.bound = calculate_bound(exclude_node, n, weights, values, capacity, value_per_weight)
        
        if exclude_node.bound > current_node.value:
            priority_queue.append(exclude_node)
            tree.add_edge(current_node, exclude_node, label="Exclude")

    # Visualization
    visualize_knapsack_tree(tree)

    return tree

def calculate_bound(node, n, weights, values, capacity, value_per_weight):
    if node.weight >= capacity:
        return 0

    bound = node.value
    remaining_capacity = capacity - node.weight
    j = node.level + 1

    while j < n and weights[value_per_weight[j][1]] <= remaining_capacity:
        bound += values[value_per_weight[j][1]]
        remaining_capacity -= weights[value_per_weight[j][1]]
        j += 1

    if j < n:
        bound += (remaining_capacity / weights[value_per_weight[j][1]]) * values[value_per_weight[j][1]]

    return bound


# Example usage:
weights = [2, 4, 1, 5, 3]
values = [6, 10, 5, 31, 100]
capacity = 5
max_value = knapsack_branch_and_bound(weights, values, capacity)
print(f"Maximum value using Branch and Bound: {max_value}")
