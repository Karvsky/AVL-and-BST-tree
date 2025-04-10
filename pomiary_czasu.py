import time
from AVL_tree import AVLTree

def create_tree_with_bisect_method():
    n_values = [5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000]
    for n in n_values:
        sorted_sequence = list(range(1, n + 1))
        tree = AVLTree()

        start_time = time.time()

        for el in sorted_sequence:
            tree.add(el)

        end_time = time.time()

        print(f"Czas tworzenia drzewa z {n} elementami: {end_time - start_time:.6f} sekund")

def find_max_element():
    tree = AVLTree()
    for el in range(1, 100000):
        tree.add(el)
    start_time = time.time()
    max_value, _ = tree.find_max()
    end_time = time.time()
    print(f"Największy element: {max_value}, Czas wyszukiwania: {end_time - start_time:.10f} sekund")

def inorder_traversal():
    tree = AVLTree()
    for el in range(1, 5000):
        tree.add(el)
    start_time = time.time()
    tree.inorder(tree.root)
    end_time = time.time()
    print('\n')
    print(f"Czas wykonania operacji in-order: {end_time - start_time:.10f} sekund")
