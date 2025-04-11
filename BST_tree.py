import math, os

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

class BSTree:
    def __init__(self):
        self.root = None

    # --- Wstawianie ---
    def insert(self, node, key):
        """Rekurencyjne wstawianie klucza do drzewa BST."""
        if not node:
            return Node(key)
        if key < node.key:
            if node.left is None: node.left = Node(key)
            else: node.left = self.insert(node.left, key)
        elif key > node.key: # Ignorujemy duplikaty
            if node.right is None: node.right = Node(key)
            else: node.right = self.insert(node.right, key)
        return node

    def add(self, key):
        """Dodaje klucz do drzewa, zaczynając od korzenia."""
        self.root = self.insert(self.root, key)

    # --- Wyszukiwanie Min/Max ---
    def get_min_value_node(self, node):
        """Znajduje węzeł z najmniejszą wartością w poddrzewie."""
        current = node
        while current and current.left is not None: current = current.left
        return current

    def find_min(self):
        """Znajduje najmniejszy klucz w całym drzewie."""
        min_node = self.get_min_value_node(self.root)
        return min_node.key if min_node else None

    def find_max(self):
        """Znajduje największy klucz w całym drzewie."""
        node = self.root
        if not node: return None
        while node.right: node = node.right
        return node.key

    # --- Usuwanie ---
    def delete(self, node, key):
        """Rekurencyjne usuwanie klucza z drzewa BST."""
        if not node: return node
        if key < node.key: node.left = self.delete(node.left, key)
        elif key > node.key: node.right = self.delete(node.right, key)
        else:
            if node.left is None: return node.right
            elif node.right is None: return node.left
            temp = self.get_min_value_node(node.right)
            node.key = temp.key
            node.right = self.delete(node.right, temp.key)
        return node

    # --- Przechodzenie drzewa ---
    def inorder(self, node):
        """Wypisuje klucze w porządku inorder."""
        if node:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        """Wypisuje klucze w porządku preorder."""
        if node:
            print(node.key, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        """Wypisuje klucze w porządku postorder."""
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key, end=" ")

    def delete_tree(self, node):
         """Rekurencyjnie usuwa poddrzewo (dla GC)."""
         if node:
             self.delete_tree(node.left)
             self.delete_tree(node.right)
             # del node # Niekonieczne

    # --- Balansowanie DSW ---
    def _rotate_right(self, parent, child):
        grand_child = child.right
        child.right = parent
        parent.left = grand_child
        return child

    def _rotate_left(self, parent, child):
        grand_child = child.left
        child.left = parent
        parent.right = grand_child
        return child

    def _tree_to_vine(self):
        count = 0
        pseudo_root = Node(None)
        pseudo_root.right = self.root
        current = pseudo_root
        while current.right is not None:
            if current.right.left is not None:
                 new_right_child = self._rotate_right(current.right, current.right.left)
                 current.right = new_right_child
            else:
                count += 1
                current = current.right
        self.root = pseudo_root.right
        return count

    def _vine_to_tree(self, size):
        if size == 0: return
        leaves = size + 1 - 2**(math.floor(math.log2(size + 1)))
        pseudo_root = Node(None)
        pseudo_root.right = self.root
        current = pseudo_root
        for _ in range(leaves):
            if current.right and current.right.right:
                new_right_child = self._rotate_left(current.right, current.right.right)
                current.right = new_right_child
                current = current.right
            else: break
        num_nodes = size - leaves
        while num_nodes > 1:
            num_nodes //= 2
            current = pseudo_root
            for _ in range(num_nodes):
                if current.right and current.right.right:
                     new_right_child = self._rotate_left(current.right, current.right.right)
                     current.right = new_right_child
                     current = current.right
                else: break
        self.root = pseudo_root.right

    def dsw_balance(self):
        if not self.root: print("Drzewo jest puste...") ; return
        print("Balansowanie DSW...")
        count = self._tree_to_vine()
        self._vine_to_tree(count)
        print("Balansowanie zakończone.")

def is_valid_int(s):
    s = s.strip()
    if not s: return False
    if s[0] in ('-', '+'): return s[1:].isdigit()
    return s.isdigit()

def bst_menu():
    os.system("cls")
    tree = BSTree()
    while True:
        print("\n--- Menu BST ---"); print("1. Wstaw element(y)"); print("2. Znajdź min"); print("3. Znajdź max") ;print("4. Usuń element"); print("5. Wypisz in-order"); print("6. Wypisz pre-order"); print("7. Wypisz post-order"); print("8. Usuń całe drzewo"); print("9. Balansuj DSW"); print("10. Wyjście")
        choice = input("Wybierz opcję: ")

        if choice == "1":
            os.system("cls")
            elements_str = input("Podaj klucze (spacją): ")
            keys_str = elements_str.split()
            valid_keys_found = False
            for k_str in keys_str:
                if is_valid_int(k_str):
                    key = int(k_str); tree.add(key); valid_keys_found = True
                else: print(f"Błąd: '{k_str}' nie jest liczbą. Pomijam.")
            if not valid_keys_found and keys_str: print("Nie wstawiono (brak prawidłowych liczb).")
        elif choice == "2": os.system("cls"); print(f"Min: {tree.find_min()}" if tree.root else "Drzewo puste.")
        elif choice == "3": os.system("cls"); print(f"Max: {tree.find_max()}" if tree.root else "Drzewo puste.")
        elif choice == "4":
             os.system("cls")
             key_str = input("Klucz do usunięcia: ")
             if is_valid_int(key_str):
                 key = int(key_str)
                 if tree.root:
                     root_before = tree.root;
                     tree.root = tree.delete(tree.root, key)
                     if not tree.root and root_before is not None: print(f"Drzewo puste (usunięto {key}?).")
                     else: print(f"Zakończono operację dla {key}.")
                 else: print("Drzewo puste.")
             else: print(f"Błąd: '{key_str}' nie jest liczbą.")
        elif choice == "5":
            os.system("cls")
            if tree.root: print("In-order: ", end=""); tree.inorder(tree.root); print()
            else: print("Drzewo puste.")
        elif choice == "6":
            os.system("cls")
            if tree.root: print("Pre-order: ", end=""); tree.preorder(tree.root); print()
            else: print("Drzewo puste.")
        elif choice == "7":
            os.system("cls")
            if tree.root: print("Post-order: ", end=""); tree.postorder(tree.root); print()
            else: print("Drzewo puste.")
        elif choice == "8": 
            os.system("cls")
            if tree.root: print("Usuwanie drzewa..."); tree.delete_tree(tree.root); tree.root = None; print("Usunięto.")
            else: print("Drzewo puste.")
        elif choice == "9": 
            os.system("cls")
            tree.dsw_balance()
            if tree.root: print("Po DSW (in-order): ", end=""); tree.inorder(tree.root); print()
            else: print("Drzewo puste.")
        elif choice == "10": break
        else: os.system("cls"); print("Nieprawidłowy wybór.")