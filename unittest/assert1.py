# assert

if __name__ == '__main__':
    try:
        #assert 10 == 10
        assert 5 == 10, 'Lo sentimos, 5 no es igual a 10'
        """ if not 5 == 10:
            raise AssertionError('Lo sentimos, cinco no es igual a diez') """
        print('>>> El programa continúa con su ejecución.')
    except AssertionError as error:
        print(error)

