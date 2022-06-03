from staycation import Staycation
from method import *

c1 = Staycation("Deluxe", "Johnny John", 2, 200)
c2 = Staycation("Single", "Betty Bett", 1, 150)
c3 = Staycation("Family", "May Flower", 2, 450)
c4 = Staycation("Deluxe", "Bobby Bob", 2, 200)
c5 = Staycation("Suite", "Alexis Alex", 2, 600)
c5 = Staycation("Single", "Paris Pear", 1, 150)

choice = print_menu()

if choice == "1":
    c1.list_all
    
elif choice == "2":
    bubble_sort()
    
elif choice == "3":
    selection_sort()
    
elif choice == "4":
    insertion_sort()
    
elif choice == "5":
    linear_search()
    
elif choice == "6":
    binary_search()
    
elif choice == "7":
    list_range()
    
