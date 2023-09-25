# Решение 10 задачи из хендбука

def Shifr(*args, **kwargs):
    mas_namber = [int(args[0][0]) + int(args[0][1]), int(args[0][1]) + int(args[0][2])]
    mas_namber.sort(reverse=1)
    print(str(mas_namber[0]) + str(mas_namber[1]))


def main():
    namber = input()
    Shifr(namber)


if __name__ == '__main__':
    main()
