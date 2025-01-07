from unittest import TestCase, main

from soy_calidad_challenge_1.product import Product
from soy_calidad_challenge_1.product_manager import ProductManager

class TestProductManager(TestCase):

    def setUp(self):
        self.pm = ProductManager()
        self.product_1 = Product('Producto A', 20.5, 50)
        self.product_2 = Product('Producto B', 30.0, 100)

    def test_add_product(self):
        self.pm.add_product(self.product_1)
        products = self.pm.read_products()
        self.assertEqual(len(products['Productos']), 1)

    def test_update_product(self):
        self.pm.add_product(self.product_1)
        product_id = list(self.pm.products.keys())[0]
        self.pm.update_product(product_id, name='Producto Actualizado', price=25.0, stock=80)
        product = self.pm.products[product_id]
        self.assertEqual(product, 'Producto Actualizado')
        self.assertEqual(self.pm.prices[product_id], 25.0)
        self.assertEqual(self.pm.stock[product_id], 80)

    def test_delete_product(self):
        self.pm.add_product(self.product_1)
        self.pm.add_product(self.product_2)
        product_id = list(self.pm.products.keys())[0]
        self.pm.delete_product(product_id)
        products = self.pm.read_products()
        self.assertNotIn(product_id, products['N°'])

if __name__ == "__main__":
    main()