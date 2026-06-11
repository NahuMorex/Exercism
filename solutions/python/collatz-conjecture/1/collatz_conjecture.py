def steps(number):
    if (number <= 0):
        raise ValueError("Only positive integers are allowed")
    pares: int = 0
    impares: int = 0
    while(number != 1):
        if (number % 2 == 0):
            pares = pares + 1
            number = number / 2
        else:
            impares = impares + 1
            number = number *3 + 1
    return pares + impares