# Решение 12 задачи из хендбука

def Is_valid_triangle(nam_1, nam_2, nam_3):
    return (nam_1 + nam_2 > nam_3)


def Is_triangle(*args, **kwargs):
    args[0].sort()
    if Is_valid_triangle(args[0][0], args[0][1], args[0][2]) and \
            Is_valid_triangle(args[0][1], args[0][2], args[0][0]) and \
            Is_valid_triangle(args[0][2], args[0][0], args[0][1]):
        print("YES")
    else:
        print("NO")


def main():
    nambers = [0, 0, 0]
    nambers[0] = int(input())
    nambers[1] = int(input())
    nambers[2] = int(input())
    Is_triangle(nambers)


if __name__ == '__main__':
    main()
