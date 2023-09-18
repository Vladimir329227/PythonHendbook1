# Решение 11 задачи из хендбука


def decoder(*args, **kwargs):
    print(args[0][1] + args[0][0] + args[0][3] + args[0][2])


def main():
    namber = input()
    decoder(namber)


if __name__ == '__main__':
    main()
