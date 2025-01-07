class Product():
    """Class responsible for product's logic."""

    def __init__(self, name: str, price: int, stock: int):
        self._name = None  
        self._price = None
        self._stock = None
        
        # USE THIS PROPERTIES WITH SETTER ENCAPSULATION METHOD
        self.name = name  
        self.price = price
        self.stock = stock

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value or not isinstance(value, str):
            raise ValueError("El nombre debe ser una cadena no vacía.")
        self._name = value
    
    @property
    def price(self) -> int:
        return self._price

    @price.setter
    def price(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("El precio debe ser un número positivo.")
        self._price = value
    
    def get_price(self) -> str:
        return str(self._price)

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("El stock debe ser un entero no negativo.")
        self._stock = value
    
    def __str__(self):
        return f"Producto({self.name}, Precio: {self.price}, Stock: {self.stock})"
