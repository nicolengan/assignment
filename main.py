from staycation import Staycation

def list_all():
    for x in data_list:
        x.return_string()


def print_menu():
    print("""1. Display all records
2. Sort record by Customer Name using Bubble sort
3. Sort record by Package Name using Selection sort
4. Sort record by Package Cost using Insertion sort
5. Search record by Customer Name using Linear Search and update record
6. Search record by Package Name using Binary Search and update record
7. List records range from $X to $Y. e.g $100-200
8. Sort record by Pax using Heap sort
Q to Exit Application""")
    
    choice = input("Enter choice (Q to exit): ")
    return choice
        
        
def validate_str(field):
    validate = True
    
    while validate:
        s = input(f"{field}: ").strip()
        sNoSpace = s.replace('', 'a')
        sNoSpace = sNoSpace.replace(' ','a')
        validate = False
        
        if not sNoSpace.isalpha():
            print("Please enter only alphabetical characters.")
            validate = True
            
    return s.lower()


def validate_int(field):
    validate = True
    
    while validate:
        
        try:
            s = int(input(f"{field}: "))
            
            if s > 0:
                validate = False
                break
            
            else:
                print("Number cannot be negative or equals to 0.")
            
        except ValueError:
            print("Please enter only numbers.")
    return s

def update_record(index_list):
    count = 1
    pkg_list = []
    
    for p in data_list:
        pkg_list.append(p.pkg_name)
        
    for i in index_list:
        
        x = 0
        obj = data_list[i]
        
        print(f"\nRecord {count}\n{'='*20}\nCustomer Name: {obj.cust_name}\nPackage Name: {obj.pkg_name}\nPax: {obj.pax}\nCost: ${obj.cost}\n")
        
        while x == False:
            
            update = validate_str("Update record (Y/N)")
            
            if update == "y":
                cust_name = validate_str("Enter new customer name (Enter nothing or space to skip)").title()
                
                while True:
                    pkg_name = validate_str("Enter new package name (Enter nothing or space to skip)").title()
                    
                    if pkg_name in pkg_list:
                        print(f"Package {pkg_name} already exists, please try again.")
                        
                    else:
                        break
                        
                pax = validate_int("Enter new pax")
                cost = validate_int("Enter new cost")
                
                data_list[i].cust_name = cust_name if cust_name else data_list[i].cust_name
                data_list[i].pkg_name = pkg_name if pkg_name else data_list[i].pkg_name
                data_list[i].pax = pax if pax else data_list[i].pax
                data_list[i].cost = cost if cost else data_list[i].cost
                
                print(f"\nNew details\n{'='*20}\nCustomer Name: {data_list[i].cust_name}\nPackage Name: {data_list[i].pkg_name}\nPax: {data_list[i].pax}\nCost: ${data_list[i].cost}\n")
                print("Update successful.")
                
                x = True
                count += 1
                
            elif update == "n":
                print("Update cancelled.")
                x = True
                count += 1
                
            else:
                print("Please only enter Y or N")


def bubble_sort():

    n = len(data_list)
    for i in range(n - 1, 0, -1):
        
        for j in range(i):
            if data_list[j].cust_name.lower() > data_list[j + 1].cust_name.lower():
                y = data_list[j]
                # swap
                data_list[j] = data_list[j + 1]
                data_list[j + 1] = y
    # add: update record to sorted display
    return data_list


def selection_sort():
    
    n = len(data_list)
    
    for i in range(n - 1):
        # Assume the ith element is the smallest.
        smallest = i
        
        # Determine if any other element contains a smaller value.
        for j in range(i + 1, n):
            if data_list[j].pkg_name.lower() < data_list[smallest].pkg_name.lower():
                smallest = j
                # Swap the ith value and smallest value only if the smallest
                # value is not already in its proper position.
                
        if smallest != i:
            y = data_list[i]
            data_list[i] = data_list[smallest]
            data_list[smallest] = y
            
    return data_list


def insertion_sort():
    
    n = len(data_list)
    # Starts with the first item as the only sorted entry.
    
    for i in range(1, n):
    # Save the value to be positioned
        value = data_list[i]
        # Find the position where value fits in the
        # ordered part of the list.
        pos = i
        
        while pos > 0 and value.cost < data_list[pos - 1].cost:
        # Shift the items to the right during the search
            data_list[pos] = data_list[pos-1]
            pos -= 1
            # Put the saved value into the open slot.
            data_list[pos] = value
            
    return data_list


def linear_search(target):
    
    bubble_sort()
    n = len(data_list)
    index_list = []
    
    for i in range(n):
    # If the target is in the ith element, return True
    
        if data_list[i].cust_name.lower() == target:
            index_list.append(data_list.index(data_list[i]))
        
        elif data_list[i].cust_name.lower() > target:
            pass
        
    if index_list:
        print(f"{len(index_list)} record(s) found! Please enter the updated records.")
        update_record(index_list)
        
    elif not index_list:
        print("Record not found, please try again.")
        return linear_search(validate_str("Enter customer name"))
            
            


def binary_search(l, r, x):
    
    selection_sort()
    index_list = []
    
    # Check base case
    if r >= l:
 
        mid = l + (r - l) // 2
 
        # If element is present at the middle itself
        
        if data_list[mid].pkg_name.lower() == x:
            index_list.append(data_list.index(data_list[mid]))
 
        # If element is smaller than mid, then it
        # can only be present in left subarray
        
        elif data_list[mid].pkg_name.lower() > x:
            return binary_search(l, mid-1, x)
 
        # Else the element can only be present
        # in right subarray
        
        else:
            return binary_search(mid + 1, r, x)
        
    if index_list:
        print("Record found! Please enter the updated records.")
        update_record(index_list)
        
    elif not index_list:
        print("Record not found, please try again.")
        return binary_search(0, len(data_list) - 1, validate_str("Enter package name"))


def list_range(start, stop):
    range_list = []
    insertion_sort()
    print(f"\nListing records from range ${start} to ${stop}")
    
    for p in data_list:
        if start <= p.cost <= stop:
            range_list.append(p)
    
    if range_list:
        for obj in range_list:
            print(f"\nCustomer Name: {obj.cust_name}\nPackage Name: {obj.pkg_name}\nPax: {obj.pax}\nCost: ${obj.cost}\n")
    else:
        print("No matching records found.\n")    

            
def heapify(heap_size, root_index):
    
    # Assume the index of the largest element is the root index
    
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # If the left child of the root is a valid index, and the element is greater
    # than the current largest element, then update the largest element
    
    if left_child < heap_size and data_list[left_child].pax > data_list[largest].pax:
        largest = left_child

    # Do the same for the right child of the root
    
    if right_child < heap_size and data_list[right_child].pax > data_list[largest].pax:
        largest = right_child

    # If the largest element is no longer the root element, swap them
    
    if largest != root_index:
        data_list[root_index], data_list[largest] = data_list[largest], data_list[root_index]
        
        # Heapify the new root element to ensure it's the largest
        
        heapify(heap_size, largest)


def heap_sort():
    n = len(data_list)

    # Create a Max Heap from the list
    # The 2nd argument of range means we stop at the element before -1 i.e.
    # the first element of the list.
    # The 3rd argument of range means we iterate backwards, reducing the count
    # of i by 1
    
    for i in range(n, -1, -1):
        heapify(n, i)

    # Move the root of the max heap to the end of
    
    for i in range(n - 1, 0, -1):
        data_list[i], data_list[0] = data_list[0], data_list[i]
        heapify(i, 0)

data_list = [
    Staycation("Johnny John", "Deluxe", 7, 300),
    Staycation("Johnny John", "Single",  9, 150),
    Staycation("May Flower", "Family", 5, 450),
    Staycation("Bobby Bob", "Ultra Deluxe", 8, 400),
    Staycation("Alexis Alex", "Suite", 6, 600),
    Staycation("Paris Pear", "Large Single", 11, 200),
    Staycation("Jane Joules", "Single Suite", 1, 350),
    Staycation("Ben Dover", "Big Family", 3, 500),
    Staycation("Mike Hawk", "Holiday", 2, 550),
    Staycation("Hugh Jass", "Deluxe Suite", 4, 800)]

while True:
    choice = print_menu().lower()
    
    if choice == "1":
        list_all()
            
    # option 2, sort record by customer name using bubble sort
    elif choice == "2":
        bubble_sort()
        list_all()
        print("Successful sort!")

    # option 3 sort record by package name using selection sort
    elif choice == "3":
        selection_sort()
        list_all()
        print("Successful sort!")

    # option 4 sort record by package cost using insertion sort
    elif choice == "4":
        insertion_sort()
        list_all()
        print("Successful sort!")

    # option 5 search record by customer name using linear search and update record
    elif choice == "5":      
        linear_search(validate_str("Enter customer name"))
        # list_all() 

    # option 6 search record by package name using binary search and update record by
    elif choice == "6":
        binary_search(0, len(data_list)-1, validate_str("Enter package name"))
        # list_all()

    elif choice == "7":
        start = validate_int("Enter start range $", False)
        stop = validate_int("Enter stop range $", False)
        
        list_range(start, stop)
        
    elif choice == "8":
        heap_sort()
        list_all()
        print("Successful sort!\n")
        
    elif choice == "q":
        break
        
    else:
        print("\nOption not found, please try again.\n")
