# Решение 1 задачи из хендбука


def dialogue(*args, **kwargs):
    print("Как Вас зовут?")
    name = input()
    print(f"Здравствуйте, {name}!")
    print("Как дела?")
    status = input()
    if status == "хорошо":
        print("Я за вас рада!")
    else:
        print("Всё наладится!")


def main():
    dialogue()


if __name__ == '__main__':
    main()
