class staycation:
    def __init__(self):
        self.__pkg_name = ""
        self.__cust_name = ""
        self.__no_pax = 0
        self.__cost = 0

    @property
    def pkg_name(self) -> str:
        return self.__pkg_name

    @property
    def cust_name(self) -> str:
        return self.__cust_name

    @property
    def no_pax(self) -> int:
        return self.__no_pax

    @property
    def cost(self) -> float:
        return self.__cost

    @pkg_name.setter
    def pkg_name(self, value: str):
        self.__pkg_name = value

    @cust_name.setter
    def cust_name(self, value: str):
        self.__cust_name = value

    @no_pax.setter
    def no_pax(self, value: int):
        self.__no_pax = value

    @cost.setter
    def cost(self, value: float):
        self.__cost = value

    def all_records():
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


