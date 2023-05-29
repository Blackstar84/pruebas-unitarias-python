from product import Product

class ShoppingCart:
    
    def __init__(self) -> None:
        # Al poner doble guión bajo significa que debe ser tratado como atributo privado
        #self.__products = list()
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def empty(self) -> bool:
        return len(self.__products) == 0


    def has_products(self):
        return not self.empty()        


