# Решение 14 задачи из хендбука

def Heresy_2(*args, **kwargs):
    nambers = sorted(list(args[0]), reverse=1)
    maximum = nambers[0] + nambers[1]
    if nambers[2] != '0':
        minimum = nambers[2] + nambers[1]
    else:
        minimum = nambers[1] + nambers[2]
    print(minimum, maximum)


def main():
    namber = input()
    Heresy_2(namber)


if __name__ == '__main__':
    main()
