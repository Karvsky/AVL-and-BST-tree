from AVL_tree import *
from pomiary_czasu import create_tree_with_bisect_method, find_max_element, inorder_traversal


print("Wybierz opcje: \n 1 AVL tree\n 2 BST tree\n 3 wyjscie")
choice = input()
if choice == "1":
    print(menu())
    print(create_tree_with_bisect_method())
    print(find_max_element())
    print(inorder_traversal())
#elif choice == '2':

elif choice == '3':
    print("Koncze program")