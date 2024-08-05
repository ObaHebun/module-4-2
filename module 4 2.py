def test_function():
    def inner_fuction():
        print('Я в области видимости функции test_function')
    return inner_fuction()

inner_function()