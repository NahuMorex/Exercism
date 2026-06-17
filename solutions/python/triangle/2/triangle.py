def is_triangle(sides):
    side_a:float=sides[0]
    side_b:float=sides[1]
    side_c:float= sides[2]
    return side_a > 0 and side_b > 0 and side_c > 0

def inequality(sides):
    side_a:float=sides[0]
    side_b:float=sides[1]
    side_c:float= sides[2]
    return side_a + side_b >= side_c and side_a + side_c >= side_b and side_b + side_c >= side_a 
    
def equilateral(sides):
    side_a:float=sides[0]
    side_b:float=sides[1]
    side_c:float= sides[2]
    return is_triangle(sides) and side_a == side_b and side_b == side_c and side_a == side_c


def isosceles(sides):
    side_a:float=sides[0]
    side_b:float=sides[1]
    side_c:float= sides[2]
    return is_triangle(sides) and inequality(sides) and (equilateral(sides) or (side_a == side_b and side_b != side_c ) or (side_a == side_c and side_b != side_c) or (side_c == side_b and side_a != side_c))

def scalene(sides):
    side_a:float=sides[0]
    side_b:float=sides[1]
    side_c:float= sides[2]
    return is_triangle(sides) and inequality(sides) and (side_a!=side_b) and (side_a!=side_c) and (side_b!=side_c)
