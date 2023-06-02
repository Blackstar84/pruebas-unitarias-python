import unittest


class TestExample(unittest.TestCase):

    def test_suma_numeros(self):
        numero1 = 10
        numero2 = 20

        resultado = numero1 + numero2
        # 30
        #Esto es lo mismo que assert como lo usabamos antes
        # Como estamos heredando de unittest podemos acceder a su método assertEqual
        # assert resultado == 30
        self.assertEqual(resultado, 30)

    def test_resta_numeros(self):
        self.assertEqual(30 - 20, 50)



if __name__ == '__main__':
    unittest.main()