# Решение 8 задачи из хендбука


def repeat_print(*args, **kwargs):
    for i in range(args[1]):
        print(f"Я больше никогда не буду писать \"{args[0]}\"!")


def main():
    namber = int(input())
    text = input()
    repeat_print(text, namber)


if __name__ == '__main__':
    main()
