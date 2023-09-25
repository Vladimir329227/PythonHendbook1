# Решение 15 задачи из хендбука

def Heresy_3(*args, **kwargs):
    nambers = sorted(list(args[0]), reverse=1)
    rez = nambers[0]
    rez += str((int(nambers[1]) + int(nambers[2])) % 10)
    rez += nambers[3]
    print(rez)


def main():
    namber = input() + input()
    Heresy_3(namber)


if __name__ == '__main__':
    main()
