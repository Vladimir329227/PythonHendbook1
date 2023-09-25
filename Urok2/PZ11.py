# Решение 11 задачи из хендбука

def Kakayata_figna(*args, **kwargs):
    mas_namber = [int(args[0][0]), int(args[0][1]), int(args[0][2])]
    mas_namber.sort()
    if mas_namber[0] + mas_namber[2] == mas_namber[1] * 2:
        print("YES")
    else:
        print("NO")


def main():
    namber = input()
    Kakayata_figna(namber)


if __name__ == '__main__':
    main()
