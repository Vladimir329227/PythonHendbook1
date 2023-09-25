# Решение 18 задачи из хендбука

def Is_pramougol(a, b, c):
    return ((a ** 2 == b ** 2 + c ** 2) or
            (b ** 2 == a ** 2 + c ** 2) or
            (c ** 2 == b ** 2 + a ** 2))


def Is_tupougolni(a, b, c):
    return ((a ** 2 > b ** 2 + c ** 2) or
            (b ** 2 > a ** 2 + c ** 2) or
            (c ** 2 > b ** 2 + a ** 2))


def Type_of_triangle(*args, **kwargs):
    if Is_pramougol(args[0], args[1], args[2]):
        print("100%")
    elif Is_tupougolni(args[0], args[1], args[2]):
        print("велика")
    else:
        print("крайне мала")


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    Type_of_triangle(a, b, c)


if __name__ == '__main__':
    main()
