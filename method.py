import gc


def print_menu():
    print("""1. Display all records
2. Sort record by Customer Name using Bubble sort
3. Sort record by Package Name using Selection sort
4. Sort record by Package Cost using Insertion sort
5. Search record by Customer Name using Linear Search and update record
6. Search record by Package Name using Binary Search and update record
7. List records range from $X to $Y. e.g $100-200
Exit Application""")
    choice = input("Enter choice: ")
    return choice


def bubble_sort(data_list):
    name_list = []
    for p in data_list:
        name_list.append(p.cust_name)

    n = len(name_list)
    for i in range(n - 1, 0, -1):
        
        for j in range(i):
            if name_list[j] > name_list[j + 1]:
                y = name_list[j]
                # swap
                name_list[j] = name_list[j + 1]
                name_list[j + 1] = y
    # add: update record to sorted display
    return name_list


def selection_sort(data_list):
    
    pkg_list = []
    
    for p in data_list:
        pkg_list.append(p.pkg_name)
        
    n = len(pkg_list)
    
    for i in range(n - 1):
        # Assume the ith element is the smallest.
        smallest = i
        
        # Determine if any other element contains a smaller value.
        for j in range(i + 1, n):
            if pkg_list[j] < pkg_list[smallest]:
                smallest = j
                # Swap the ith value and smallest value only if the smallest
                # value is not already in its proper position.
                
        if smallest != i:
            y = pkg_list[i]
            pkg_list[i] = pkg_list[smallest]
            pkg_list[smallest] = y
            
    return pkg_list


def insertion_sort(data_list):
    cost_list = []
    for p in data_list:
        cost_list.append(p.cost)
        
    n = len(cost_list)
    # Starts with the first item as the only sorted entry.
    
    for i in range(1, n):
    # Save the value to be positioned
        value = cost_list[i]
        # Find the position where value fits in the
        # ordered part of the list.
        pos = i
        
        while pos > 0 and value < cost_list[pos - 1]:
        # Shift the items to the right during the search
            cost_list[pos] = cost_list[pos-1]
            pos -= 1
            # Put the saved value into the open slot.
            cost_list[pos] = value
            
    return cost_list


def linear_search():
    pass


def binary_search():
    pass


def list_range():
    pass


x = 0
