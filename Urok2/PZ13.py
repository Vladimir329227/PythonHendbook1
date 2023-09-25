# Решение 13 задачи из хендбука

def Heresy(*args, **kwargs):
    oll_nambers = "1234567890"
    for i in range(len(args[0])):
        for o in range(len(oll_nambers)):
            if oll_nambers[o] not in args[0][i]:
                oll_nambers = oll_nambers.replace(oll_nambers[o], ' ')
    oll_nambers = oll_nambers.replace(' ', '')
    print(oll_nambers[0])


def main():
    nambers = ["", "", ""]
    nambers[0] = input()
    nambers[1] = input()
    nambers[2] = input()
    Heresy(nambers)


if __name__ == '__main__':
    main()
