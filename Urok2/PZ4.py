# Решение 4 задачи из хендбука

def viner(*args, **kwargs):
    args[0].sort(key=lambda i: i[0], reverse=1)
    for i in range(len(args[0])):
        print(f"{i + 1}. {args[0][i][1]}")


def main():
    speed_p = [int(input()), "Петя"]
    speed_v = [int(input()), "Вася"]
    speed_t = [int(input()), "Толя"]

    viner([speed_p, speed_v, speed_t])


if __name__ == '__main__':
    main()
