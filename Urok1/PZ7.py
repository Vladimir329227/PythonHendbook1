# Решение 7 задачи из хендбука


def repeat_print(*args, **kwargs):
    for i in range(args[1]):
        print(args[0])


def main():
    namber = int(input())
    text = "Купи слона!"
    repeat_print(text, namber)


if __name__ == '__main__':
    main()
