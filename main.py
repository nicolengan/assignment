from staycation import Staycation
from method import *

def list_all():
    for x in data_list:
        x.return_string()
        
        
c1 = Staycation("Johnny John", "Deluxe", 7, 300)
c2 = Staycation("Johnny John", "Single",  9, 150)
c3 = Staycation("May Flower", "Family", 5, 450)
c4 = Staycation("Bobby Bob", "Ultra Deluxe", 8, 400)
c5 = Staycation("Alexis Alex", "Suite", 6, 600)
c6 = Staycation("Paris Pear", "Large Single", 11, 200)
c7 = Staycation("Jane Joules", "Single Suite", 1, 350)
c8 = Staycation("Ben Dover", "Big Family", 3, 500)
c9 = Staycation("Mike Hawk", "Holiday", 2, 550)
c10 = Staycation("Hugh Jass", "Deluxe Suite", 4, 800)

data_list = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

while True:
    choice = print_menu().lower()
    if choice == "1":
        list_all()
        print("Successful sort!")
            
            
    # option 2, sort record by customer name using bubble sort
    elif choice == "2":
        bubble_sort(data_list)
        list_all()
        print("Successful sort!")

    # option 3 sort record by package name using selection sort
    elif choice == "3":
        selection_sort(data_list)
        list_all()
        print("Successful sort!")

    # option 4 sort record by package cost using insertion sort
    elif choice == "4":
        insertion_sort(data_list)
        list_all()
        print("Successful sort!")

    # option 5 search record by customer name using linear search and update record
    elif choice == "5":      
        linear_search(data_list, validate_str("Enter customer name"))
        # list_all() 

    # option 6 search record by package name using binary search and update record by
    elif choice == "6":
                
        binary_search(data_list, 0, len(data_list)-1, validate_str("Enter package name"))
        # list_all()

    elif choice == "7":
        
        start = validate_int("Enter start range $")
        stop = validate_int("Enter stop range $")
        
        list_range(data_list, start, stop)
        
    elif choice == "8":
        
        heap_sort(data_list)
        list_all()
        break
        
    elif choice == "q":
        
        break
        
    else:
        print("\nOption not found, please try again.\n")
        pass
