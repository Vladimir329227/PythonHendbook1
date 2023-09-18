# Решение 20 задачи из хендбука


def calculation(*args, **kwargs):
    price = args[0] * args[1]
    delta = price - args[0] * min(args[2], args[3])
    rez_max = delta / (max(args[2], args[3]) - min(args[2], args[3]))
    if max(args[2], args[3]) == args[2]:
        print(f"{int(rez_max)} {int(args[0] - rez_max)}")
    else:
        print(f"{int(args[0] - rez_max)} {int(rez_max)}")


def main():
    namber_a = int(input())
    namber_b = int(input())
    namber_c = int(input())
    namber_d = int(input())
    calculation(namber_a, namber_b, namber_c, namber_d)


if __name__ == '__main__':
    main()
