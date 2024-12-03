

def sumar(x, y):
    return x + y


def restar(x, y):
    return x - y


def multiplicar(x, y):
    return x * y


def dividir(x, y):
    if y == 0:
        raise ValueError("No se puede dividir por cero")
    return x / y

