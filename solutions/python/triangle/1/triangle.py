def is_triangle(sides):
    a:float=sides[0]
    b:float=sides[1]
    c:float= sides[2]
    return a > 0 and b > 0 and c > 0

def inequality(sides):
    a:float=sides[0]
    b:float=sides[1]
    c:float= sides[2]
    return a + b >= c and a + c >= b and b + c >= a 
    
def equilateral(sides):
    a:float=sides[0]
    b:float=sides[1]
    c:float= sides[2]
    return is_triangle(sides) and a == b and b == c and a == c


def isosceles(sides):
    a:float=sides[0]
    b:float=sides[1]
    c:float= sides[2]
    return is_triangle(sides) and inequality(sides) and (equilateral(sides) or (a == b and b != c ) or (a == c and b != c) or (c == b and a != c))

def scalene(sides):
    a:float=sides[0]
    b:float=sides[1]
    c:float= sides[2]
    return is_triangle(sides) and inequality(sides) and (a!=b) and (a!=c) and (b!=c)
