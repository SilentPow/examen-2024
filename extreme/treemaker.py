import random

def create_christmas_tree(height):
    tree = []

    for i in range(height):
        row = [' '] * (2 * height - 1)
        for j in range(height - i - 1, height + i):
            row[j] = '*'

            # Add decorations randomly
            if i > 0 and random.random() < 0.2:
                row[j] = 'o'
            elif i > 0 and random.random() < 0.1:
                row[j] = 'O'

        tree.append(row)

    # Add trunk
    trunk_height = height // 3
    trunk_width = height // 3
    trunk_start = (2 * height - 1 - trunk_width) // 2
    for i in range(trunk_height):
        tree.append([' '] * (2 * height - 1))
        tree[-1][trunk_start:trunk_start + trunk_width] = ['#'] * trunk_width

    return tree

def print_christmas_tree(tree):
    for row in tree:
        print(' '.join(row))

# Set the height of the Christmas tree
tree_height = 10

# Create and print the Christmas tree
christmas_tree = create_christmas_tree(tree_height)
print_christmas_tree(christmas_tree)
