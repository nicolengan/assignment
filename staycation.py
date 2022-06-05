class Staycation:
    def __init__(self, cust_name, pkg_name, pax, cost):
        self.__cust_name = cust_name
        self.__pkg_name = pkg_name
        self.__pax = pax
        self.__cost = cost
        
    @property
    def cust_name(self) -> str:
        return self.__cust_name
    @property
    def pkg_name(self) -> str:
        return self.__pkg_name  

    @property
    def pax(self) -> int:
        return self.__pax

    @property
    def cost(self) -> float:
        return self.__cost
    
    @cust_name.setter
    def cust_name(self, value: str):
        self.__cust_name = value
        
    @pkg_name.setter
    def pkg_name(self, value: str):
        self.__pkg_name = value

    @pax.setter
    def pax(self, value: int):
        self.__pax = value

    @cost.setter
    def cost(self, value: float):
        self.__cost = value
    
    def return_string(self):
        return print(f"Customer Name: {self.__cust_name}\nPackage Name: {self.__pkg_name}\nPax: {self.__pax}\nCost: ${self.__cost}\n")
