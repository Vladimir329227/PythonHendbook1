# Решение 13 задачи из хендбука


def summ(*args, **kwargs):
    print(args[1] // args[0])
    print(args[1] % args[0])


def main():
    namber_a = int(input())
    namber_b = int(input())
    summ(namber_a, namber_b)


if __name__ == '__main__':
    main()
