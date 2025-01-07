from tabulate import tabulate
from .product import Product

class ProductManager():
    """Clase para manejar la lógica CRUD de productos."""

    def __init__(self):
        self.products = dict()
        self.prices = dict()
        self.stock = dict()
        self.next_id = 1   # ID autoincremental para productos
        
    def add_product(self, product: Product):
        """Crear un producto nuevo y añadirlo a la lista."""
        self.products[self.next_id]=product.name
        self.prices[self.next_id]= product.price
        self.stock[self.next_id]=product.stock
        self.next_id += 1
    
    def get_values_as_list(self, column: dict, index: bool = False) -> list:
        elements = list()
        for i in column:
            if index:
                elements.append(i)
            else:
                elements.append(column[i])
        return elements

    def read_products(self):
        indexes = self.get_values_as_list(self.products, True)
        products = self.get_values_as_list(self.products)
        prices = self.get_values_as_list(self.prices)
        stock = self.get_values_as_list(self.stock)
        print('='*50)
        print('Lista de Productos: ')
        print('='*50)
        if self.products:
            print(tabulate({
                'N°': indexes,
                'Productos': products,
                'Precios': prices,
                'Stock': stock
            }, headers='keys', tablefmt='fancy_grid'))
        else:
            print('No hay productos para mostrar.')

    def update_product(self, product_id, name=None, price=None, stock=None):
        """Actualizar los detalles de un producto por ID."""
        for product in self.products:
            if product["id"] == product_id:
                if name is not None:
                    product["name"] = name
                if price is not None:
                    product["price"] = price
                if stock is not None:
                    product["stock"] = stock
                return
        raise ValueError("Producto con el ID especificado no encontrado.")

    def delete_product(self, product_id):
        """Eliminar un producto por ID."""
        for product in self.products:
            if product["id"] == product_id:
                self.products.remove(product)
                return
        raise ValueError("Producto con el ID especificado no encontrado.")