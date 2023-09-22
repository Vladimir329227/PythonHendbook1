# Решение 2 задачи из хендбука


def viner(*args, **kwargs):
    if args[0] > args[1]:
        print("Петя")
    else:
        print("Вася")


def main():
    speed_p = int(input())
    speed_v = int(input())
    viner(speed_p, speed_v)


if __name__ == '__main__':
    main()
