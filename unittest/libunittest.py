import unittest


class Example(unittest.TestCase):

    def test_suma_numeros(self):
        numero1 = 10
        numero2 = 20

        resultado = numero1 + numero2
        # 30

        self.assertEqual(resultado, 30)


        
