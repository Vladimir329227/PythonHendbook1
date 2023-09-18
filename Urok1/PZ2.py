# Решение 2 задачи из хендбука

def print_question(*args, **kwargs):
    print("Как Вас зовут?")


def print_hellow(*args, **kwargs):
    print("Привет, " + args[0])


def main():
    print_question()
    name = input()
    print_hellow(name)


if __name__ == '__main__':
    main()
