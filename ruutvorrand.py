import math


def quadratic_equation(a:int, b:int, c:int):
    # Siia tulevad erinevad vahesammud
    # x1:int tähistab seda et funktsiooni parameeteetri väärtus peaks olema number (integer).
    discriminant = b**2 - 4*a*c
    if discriminant < 0:    
        print("Discriminant is negative, unable to continue.")
        quit()
    sqrt = math.sqrt(discriminant)
    x1 = (-b + sqrt) / (2*a) # mingi lõplik sisu.
    x2 = (-b - sqrt) / (2*a) # mingi lõplik sisu.
    return x1, x2  # Funktsioonid saavad anda tagasi ka mitu väärtust korraga.


if __name__ == "__main__":
    # 6x² + 11x - 35 = 0 
    x1, x2 = quadratic_equation(6, 11, -35)
    print("x1 " + str(x1))
    print("x2 " + str(x2))
    # 3x² + 2x + 1 = 0 
    x1, x2 = quadratic_equation(3, 2, 1)
    print("x1 " + str(x1))
    print("x2 " + str(x2))

