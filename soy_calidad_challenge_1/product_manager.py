from .product import Product

class ProductManager():
    """Class to handle Products CRUD."""

    def __init__(self):
        self.products = dict()
        self.prices = dict()
        self.stock = dict()
        self.next_id = 1
    

    def add_product(self, product: Product):
        """Add a new product and add it to its respective dictionary."""
        self.products[self.next_id]=product.name
        self.prices[self.next_id]= product.price
        self.stock[self.next_id]=product.stock
        self.next_id += 1


    def read_products(self):
        '''Get all products as a dictionary'''       
        indexes = list(self.products.keys())
        products = list(self.products.values())
        prices = list(self.prices.values())
        stock = list(self.stock.values())
        data = None
        if self.products:
            data = {
                'N°': indexes,
                'Productos': products,
                'Precios': prices,
                'Stock': stock
            }
        return data

    def update_product(self, product_id: int, name=None, price=None, stock=None) -> bool:
        '''Update a product by its id.'''
        result = False
        product = self.products.get(product_id)
        if product:
            self.products[product_id] = name if name is not None else self.products[product_id]
            self.prices[product_id] = price if price is not None else self.prices[product_id]
            self.stock[product_id] = stock if stock is not None else self.stock[product_id]
            result = True
        return result
        #raise ValueError('Producto con el ID especificado no encontrado.')

    def delete_product(self, product_id: int) -> bool:
        """Delete a product by Id."""
        result = False
        product = self.products.get(product_id)
        if product:
            self.products.pop(product_id)
            self.prices.pop(product_id)
            self.stock.pop(product_id)
            result = True
        return result
        #raise ValueError("Producto con el ID especificado no encontrado.")