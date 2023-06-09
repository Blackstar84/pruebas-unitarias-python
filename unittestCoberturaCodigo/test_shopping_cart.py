import unittest

from product import Product, ProductDiscountError
from shopping_cart import ShoppingCart


class TestShoppingCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('>>> El método de clase setUpClass se ejecuta antes de todas las pruebas.')

    @classmethod
    def tearDownClass(cls):
        print('>>> El método de clase tearDownClass se ejecuta después de todas las pruebas.')


    def setUp(self) -> None:
        self.name = 'Iphone'
        self.price = 500.00
        self.smartphone = Product(self.name, self.price)

        self.shopping_cart_1 = ShoppingCart()
        self.shopping_cart_2 = ShoppingCart()
        self.shopping_cart_2.add_product(self.smartphone)



    def tearDown(self) -> None:
        print('>>> El método tearDown se ejecuta después de cada una de las pruebas.')


    def test_product_object(self):
        name = 'Manzana'
        price = 1.70
        product = Product(name, price)

        self.assertEqual(product.name, name)
        self.assertEqual(product.price, price)
        #self.assertEqual(product.price, 10.0, 'Lo sentimos, el precio no es el mismo')

    def test_product_name(self):
        self.assertEqual(self.smartphone.name, self.name)
    
    def test_product_price(self):    
        self.assertEqual(self.smartphone.price, self.price)

    def test_shopping_cart_empty(self):
        self.assertTrue(self.shopping_cart_1.empty(), 'Lo sentimos el carrito de compras no se encuentra vacío.')    

    def test_shopping_cart_has_product(self):
        self.assertTrue(self.shopping_cart_2.has_products())
        self.assertFalse(self.shopping_cart_2.empty())


    def test_product_in_shopping_cart(self):
        product = Product('Nuevo producto', 10)
        self.shopping_cart_2.add_product(product)

        self.assertIn(product, self.shopping_cart_2.products)
        self.assertIn(self.smartphone, self.shopping_cart_2.products)

        

    def test_product_not_in_shopping_Cart(self):
        self.shopping_cart_2.remove_product(self.smartphone)

        self.assertNotIn(self.smartphone, self.shopping_cart_2.products)

    def test_discount_error(self):
        with self.assertRaises(ProductDiscountError):
            Product(name='Example', price=10.0, discount=11.0)


    def test_total_shopping_cart(self):
        self.shopping_cart_1.add_product(Product(name='Libro', price=15.0))
        self.shopping_cart_1.add_product(Product(name='Cámara', price=700.0, discount=70))
        self.shopping_cart_1.add_product(Product(name='PC', price=1000, discount=0.0))

        self.assertGreater(self.shopping_cart_1.total, 0) # > permite evaluar mayor que  
        self.assertLess(self.shopping_cart_1.total, 2000) # < permite evaluar menor que 

        self.assertEqual(self.shopping_cart_1.total, 1645)

        # assertGreaterEqual >=
        # assertLessEqual <=

    def test_total_empty_shopping_cart(self):
        self.assertEqual(self.shopping_cart_1.total, 0.0)    
        

    def test_code_product(self):
        self.assertRegex(self.smartphone.code, self.smartphone.name, 'Lo sentimos, el código no cumple con la expresión.')
