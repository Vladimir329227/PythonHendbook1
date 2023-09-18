# Решение 19 задачи из хендбука


def handing_print(*args, **kwargs):
    """Рассчет cдачи с покупки
       сдача покупки = получено денег - вес покупки * цена
       """

    print(
        f"================Чек================\n\
Товар:{' ' * (35 - 6 - len(args[3]))}{args[3]}\n\
Цена:{' ' * (35 - 5 - len(f'{args[1]}кг * {args[0]}руб/кг'))}{args[1]}кг * {args[0]}руб/кг\n\
Итого:{' ' * (35 - 6 - len(f'{args[0] * args[1]}руб'))}{args[0] * args[1]}руб\n\
Внесено:{' ' * (35 - 8 - len(f'{args[2]}руб'))}{args[2]}руб\n\
Сдача:{' ' * (35 - 6 - len(f'{args[2] - args[0] * args[1]}руб'))}{args[2] - args[0] * args[1]}руб\n\
===================================")


def main():
    name = input()
    price = int(input())
    weight = int(input())
    namber = int(input())
    handing_print(price, weight, namber, name)


if __name__ == '__main__':
    main()
