# Решение 14 задачи из хендбука


def summ(*args, **kwargs):
    print(args[0] + args[2] + 1)


def main():
    namber_a = int(input())
    namber_b = int(input())
    namber_c = int(input())
    summ(namber_a, namber_b, namber_c)


if __name__ == '__main__':
    main()
