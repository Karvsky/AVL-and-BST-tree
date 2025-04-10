class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
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

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        return y

    def balance(self, node):
        balance = self.balance_factor(node)

        if balance > 1:
            if self.balance_factor(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1:
            if self.balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def insert(self, root, key):
        if root is None:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        return self.balance(root)

    def search(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        return self.balance(root)

    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    def in_order(self, root):
        return self.in_order(root.left) + [root.key] + self.in_order(root.right) if root else []

    def pre_order(self, root):
        return [root.key] + self.pre_order(root.left) + self.pre_order(root.right) if root else []

    def post_order(self, root):
        return self.post_order(root.left) + self.post_order(root.right) + [root.key] if root else []

    def print_search_path(self, root, key):
        path = []
        while root:
            path.append(root.key)
            if key < root.key:
                root = root.left
            elif key > root.key:
                root = root.right
            else:
                break
        return path

    def print_in_order(self):
        return self.in_order(self.root)

    def print_pre_order(self):
        return self.pre_order(self.root)

    def print_post_order(self):
        return self.post_order(self.root)


def menu():
    tree = AVLTree()
    while True:
        print("\n1. Wstaw element")
        print("2. Wyszukaj element")
        print("3. Usun element")
        print("4. Wypisz drzewo w porzadku in-order")
        print("5. Wypisz drzewo w porzadku pre-order")
        print("6. Wypisz drzewo w porzadku post-order")
        print("7. Usun cale drzewo")
        print("8. Wywaz drzewo")
        print("9. Zakoncz")

        option = input("Wybierz opcje: ")

        if option == '1':
            n = int(input("Ile elementow chcesz wstawic? (maksymalnie 10) "))
            if n > 10:
                print("Maksymalna liczba elementow to 10. Zostalo wstawionych 10 elementow.")
                n = 10
            for i in range(n):
                while True:
                    try:
                        key = int(input("Wpisz element (liczba calkowita): "))
                        tree.root = tree.insert(tree.root, key)
                        break
                    except ValueError:
                        print("Blad: Wpisz prawidlowa liczbe calkowita.")
            print("Elementy zostaly dodane.")

        elif option == '2':
            try:
                key = int(input("Podaj wartosc do wyszukania: "))
                path = tree.print_search_path(tree.root, key)
                print(f"Sciezka do {key}: {path}")
            except ValueError:
                print("Blad: Wpisz prawidlowa liczbe calkowita.")

        elif option == '3':
            try:
                n = int(input("Ile elementow chcesz usunac? "))
                if n > 10:
                    print("Maksymalna liczba elementow to 10. Zostalo usunietych 10 elementow.")
                    n = 10
                for _ in range(n):
                    while True:
                        try:
                            key = int(input("Podaj wartosc do usuniecia: "))
                            tree.root = tree.delete(tree.root, key)
                            break
                        except ValueError:
                            print("Blad: Wpisz prawidlowa liczbe calkowita.")
                print("Elementy zostaly usuniete.")
            except ValueError:
                print("Blad: Wpisz prawidlowa liczbe calkowita.")

        elif option == '4':
            print(f"Drzewo w porzadku in-order: {tree.print_in_order()}")

        elif option == '5':
            print(f"Drzewo w porzadku pre-order: {tree.print_pre_order()}")

        elif option == '6':
            print(f"Drzewo w porzadku post-order: {tree.print_post_order()}")

        elif option == '7':
            tree.root = None
            print("Cale drzewo zostalo usuniete.")

        elif option == '8':
            print("Rownowazenie drzewa.")

        elif option == '9':
            print("Koncze program.")
            break

        else:
            print("Nieprawidlowa opcja!")


#if __name__ == "__main__":
    #menu()