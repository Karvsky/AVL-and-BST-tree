from AVL_tree import *
from BST_tree import *
from pomiary_czasu import create_tree_with_bisect_method, find_max_element, inorder_traversal


print("Wybierz opcje: \n 1 AVL tree\n 2 BST tree\n 3 wyjscie")
temp = True
while temp:
    choice = input("Wybór: ")    
    if choice == "1":
        print(menu())
        print(create_tree_with_bisect_method())
        print(find_max_element())
        print(inorder_traversal())
        temp = False    
    elif choice == '2':
        bst_menu()
        temp = False    
    elif choice == '3':
        print("Koncze program")
        temp = False    
    else: 
        print("Zły wybór, wybierz ponownie")
        