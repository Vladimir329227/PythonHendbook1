# Решение 3 задачи из хендбука

def viner(*args, **kwargs):
    if args[1][1] < args[0][1] > args[2][1]:
        print(args[0][0])
    elif args[2][1] < args[1][1] > args[0][1]:
        print(args[1][0])
    else:
        print(args[2][0])


def main():
    speed_p = ["Петя", int(input())]
    speed_v = ["Вася", int(input())]
    speed_t = ["Толя", int(input())]

    viner(speed_p, speed_v, speed_t)


if __name__ == '__main__':
    main()
