# Решение 5 задачи из хендбука

def viner(*args, **kwargs):
    args[0].sort(key=lambda i: i[0], reverse=1)
    print(f"{args[0][0][1]}")


def main():
    apple_p = [int(input()) + 6, "Петя"]
    apple_v = [int(input()) + 12, "Вася"]

    viner([apple_p, apple_v])


if __name__ == '__main__':
    main()
