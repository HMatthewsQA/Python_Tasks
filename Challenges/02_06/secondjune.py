def factorial(number):
    generated = 1
    while number > 0:
        generated = generated * number
        number -= 1
    return generated