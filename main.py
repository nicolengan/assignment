from pprint import pprint
from assignment import staycation


def all_records():
    for i in vars(c1):
        print(i.replace("staycation", ""))
        print(vars(c1)[i])
    pass

def bubble_sort():
    pass


def selection_sort():
    pass


def insertion_sort():
    pass


def linear_search():
    pass


def binary_search():
    pass


def list_range():
    pass


c1 = staycation()
c1.pkg_name = "Deluxe"
c1.cust_name = "Banana"
c1.no_pax = 2
c1.cost = 200

print(vars(c1))
# all_records()