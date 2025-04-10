import time
import random
from AVL_tree import AVLTree

# Funkcja do generowania posortowanych ciągów liczb naturalnych
def generate_sorted_sequences(n):
    return sorted(random.sample(range(1, 10 * n), n))

# Funkcja do mierzenia czasu operacji na drzewie
def measure_avl_operations():
    for n in [10, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]:
        sequence = generate_sorted_sequences(n)
        tree = AVLTree()

        # Mierzymy czas wstawiania elementów
        start_time = time.time()
        for num in sequence:
            tree.add(num)
        end_time = time.time()
        print(f"Czas wstawiania {n} elementów: {end_time - start_time:.6f} sekund")

        # Mierzymy czas wyszukiwania elementu o maksymalnej wartości
        start_time = time.time()
        max_value, path = tree.find_max()
        end_time = time.time()
        print(f"Czas wyszukiwania maksymalnej wartości ({max_value}): {end_time - start_time:.6f} sekund")

        # Mierzymy czas wypisania wszystkich elementów drzewa w porządku in-order
        start_time = time.time()
        tree.inorder(tree.root)
        end_time = time.time()
        print(f"Czas wypisania {n} elementów w porządku in-order: {end_time - start_time:.6f} sekund")

if __name__ == "__main__":
    measure_avl_operations()
