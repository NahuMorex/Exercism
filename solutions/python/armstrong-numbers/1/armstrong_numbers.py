def number_of_cifers(number):
    cifers:int = 1
    while number //10 != 0:
        cifers = cifers +1
        number = number //10
    return cifers

def armstrong_algoritm(number):
    cifers: int = number_of_cifers(number)
    armstrong: int = 0
    while number // 10 != 0:
        armstrong = armstrong + (number % 10) ** cifers
        number = number // 10
    armstrong = armstrong + number ** cifers
    return armstrong

def is_armstrong_number(number):
    return armstrong_algoritm(number) == number