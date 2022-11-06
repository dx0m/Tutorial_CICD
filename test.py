from payment import *


def test(a, b):
    c = calculation(a, b)
    test_c = a+b
    assert c == test_c

#Новый тест
def test_new_function(a, b, c):
    x = new_function(a, b, c)
    test_x = a*b/c
    assert x == test_x

test(10, 20)
test(1, 15)
test(40, 150)

test_new_function(2, 3, 4)
test_new_function(20, 30, 40)
test_new_function(10,20,'x')