from unittest import TestCase, main

from soy_calidad_challenge_1.product import Product

class TestProduct(TestCase):

    def test_create_valid_product(self):
        product = Product('Producto A', 20.5, 50)
        self.assertEqual(product.name, 'Producto A')
        self.assertEqual(product.price, 20.5)
        self.assertEqual(product.stock, 50)

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            Product('', 20.5, 50)

    def test_invalid_price(self):
        with self.assertRaises(ValueError):
            Product('Producto A', -20.5, 50)

    def test_invalid_stock(self):
        with self.assertRaises(ValueError):
            Product('Producto A', 20.5, -50)

if __name__ == "__main__":
    main()
