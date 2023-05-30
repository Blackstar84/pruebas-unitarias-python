"""
    Para que una clase sea considerada un error debe heredar de Exception
"""
class ProductDiscountError(Exception):
    pass

class Product:

    def __init__(self, name: str, price: float, discount: float = 0.0) -> None:
        self.name = name
        self.price = price
        if discount > price:
            raise ProductDiscountError('Lo sentimos, el descuento no pude ser mayor al precio.')
        
        self.discount = discount

    @property # convertimos el método en un atributo
    def code(self):
        return f'code-{self.name}'      