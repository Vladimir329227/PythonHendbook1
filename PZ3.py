# Решение 3 задачи из хендбука


def repeat_print(*args, **kwargs):
    for i in range(3):
        print(args[0])


def main():
    text = input()
    repeat_print(text)


if __name__ == '__main__':
    main()
