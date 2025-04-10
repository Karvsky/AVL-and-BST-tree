class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.height = 1 


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        return y

    def balance(self, node):
        balance_factor = self.balance_factor(node)

        if balance_factor > 1:
            if self.balance_factor(node.left) < 0:
                node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance_factor < -1:
            if self.balance_factor(node.right) > 0:
                node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def insert(self, node, key):
        if not node:
            return Node(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        return self.balance(node)

    def delete(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            min_node = self.get_min_value_node(node.right)
            node.key = min_node.key
            node.right = self.delete(node.right, min_node.key)

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        return self.balance(node)

    def get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.get_min_value_node(node.left)

    def find_min(self):
        node = self.get_min_value_node(self.root)
        if node:
            path = []
            self._find_min_path(self.root, node.key, path)
            return node.key, path
        return None, []

    def find_max(self):
        node = self.root
        path = []
        while node:
            path.append(node.key)
            if node.right:
                node = node.right
            else:
                break
        return node.key, path

    def _find_min_path(self, node, key, path):
        if node is None:
            return False
        path.append(node.key)
        if node.key == key:
            return True
        elif key < node.key:
            return self._find_min_path(node.left, key, path)
        else:
            return self._find_min_path(node.right, key, path)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.key, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def delete_tree(self, node):
        if node:
            self.delete_tree(node.left)
            self.delete_tree(node.right)
            print(f"Usunięto: {node.key}")
            del node

    def dsw_balance(self):
        nodes = []
        self.flatten_tree(self.root, nodes)
        self.root = self.build_balanced_tree(nodes)

    def flatten_tree(self, node, nodes):
        if node:
            self.flatten_tree(node.left, nodes)
            nodes.append(node)
            node.left = None
            self.flatten_tree(node.right, nodes)

    def build_balanced_tree(self, nodes):
        def build(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            node = nodes[mid]
            node.left = build(start, mid - 1)
            node.right = build(mid + 1, end)
            node.height = 1 + max(self.height(node.left), self.height(node.right))
            return node

        return build(0, len(nodes) - 1)

    def add(self, key):
        self.root = self.insert(self.root, key)


def menu():
    tree = AVLTree()
    while True:
        print("\nMenu:")
        print("1. Wstaw element do drzewa")
        print("2. Wyszukaj najmniejszy element")
        print("3. Wyszukaj największy element")
        print("4. Usun element")
        print("5. Wypisz drzewo w porządku in-order")
        print("6. Wypisz drzewo w porządku pre-order")
        print("7. Usuń całe drzewo")
        print("8. Balansowanie drzewa (algorytm DSW)")
        print("9. Wyjście")

        choice = input("Wybierz opcję: ")

        try:
            if choice == "1":
                n = int(input("Ile elementów chcesz dodać? "))
                for _ in range(n):
                    key = int(input("Podaj wartość klucza: "))
                    tree.add(key)

            elif choice == "2":
                min_value, path = tree.find_min()
                if min_value:
                    print(f"Najmniejszy element: {min_value} (Ścieżka: {path})")
                else:
                    print("Drzewo jest puste.")

            elif choice == "3":
                max_value, path = tree.find_max()
                print(f"Największy element: {max_value} (Ścieżka: {path})")

            elif choice == "4":
                key = int(input("Podaj wartość klucza do usunięcia: "))
                tree.root = tree.delete(tree.root, key)
                print(f"Usunięto element {key}")

            elif choice == "5":
                print("Drzewo w porządku in-order: ", end="") 
                tree.inorder(tree.root)
                print()

            elif choice == "6":
                print("Drzewo w porządku pre-order: ", end="") 
                tree.preorder(tree.root)
                print()

            elif choice == "7":
                print("Usuwanie całego drzewa...")
                tree.delete_tree(tree.root)
                tree.root = None

            elif choice == "8":
                tree.dsw_balance()
                print("Drzewo zostało zbalansowane metodą DSW")

            elif choice == "9":
                print("Wyjście z programu...")
                break

            else:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")

        except Exception as e:
            print(f"Błąd: {e}")