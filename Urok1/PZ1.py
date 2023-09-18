# Решение 1 задачи из хендбука

def print_text(*args, **kwargs):
    print(args[0])


def main():
    text = "Привет, Яндекс!"
    print_text(text)


if __name__ == '__main__':
    main()
