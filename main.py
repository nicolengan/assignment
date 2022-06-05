"""
extra feature: heap sort/jump search?
to do: change data_list after sorted, error handling, optimise bubble sort and linear search?
https://stackabuse.com/search-algorithms-in-python/
https://stackabuse.com/sorting-algorithms-in-python/
"""

from staycation import Staycation
from method import *

c1 = Staycation("Deluxe", "Johnny John", 2, 200)
c2 = Staycation("Single", "Betty Bett", 1, 150)
c3 = Staycation("Family", "May Flower", 2, 450)
c4 = Staycation("Deluxe", "Bobby Bob", 2, 200)
c5 = Staycation("Suite", "Alexis Alex", 2, 600)
c6 = Staycation("Single", "Paris Pear", 1, 150)
c7 = Staycation("Suite", "Jane Joules", 2, 600)
c8 = Staycation("Family", "Ben Dover", 2, 450)
c9 = Staycation("Single", "Mike Hawk", 1, 150)
c10 = Staycation("Single", "Hugh Jass", 1, 150)

data_list = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

choice = print_menu()

if choice == "1":
    for x in data_list:
        x.list_all()
    # for x in data_list:
    #     print(x.cust_name)
    #     print(data_list.index(x))
        
# option 2, sort record by customer name using bubble sort
elif choice == "2":
   print(bubble_sort(data_list))

# option 3 sort record by package name using selection sort
elif choice == "3":
    print(selection_sort(data_list))
    for x in data_list:
        x.list_all()

# option 4 sort record by package cost using insertion sort
elif choice == "4":
    print(insertion_sort(data_list))

# option 5 search record by customer name using linear search and update record
elif choice == "5":
    linear_search()

# option 6 search record by package name using binary search and update record by
elif choice == "6":
    binary_search()

elif choice == "7":
    list_range()
    
else:
    print
