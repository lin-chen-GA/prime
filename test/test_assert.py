#!/usr/bin/python

from primepackage import is_prime

def test_numbers():

    try:
        response = is_prime(1)
        assert response == False
    except Exception as err:
        print(err)

    try:
        response = is_prime(2)
        assert response == True
    except Exception as err:
        print(err)

    try:
        response = is_prime(3.14)
    except Exception as err:
        print(err)
