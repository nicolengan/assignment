class Staycation:
    def __init__(self, pkg_name, cust_name, no_pax, cost):
        self.__pkg_name = pkg_name
        self.__cust_name = cust_name
        self.__no_pax = no_pax
        self.__cost = cost

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
    
    def list_all(self):
        print(f"Package Name: {self.__pkg_name}\nCustomer Name: {self.__cust_name}\nPax: {self.__no_pax}\nCost: {self.__cost}\n")
