# Решение 6 задачи из хендбука


def handing_print(*args, **kwargs):
    """Рассчет cдачи с покупки
       сдача покупки = получено денег - вес покупки * цена
       """

    print(
        f"Чек\n\
{args[3]} - {args[1]}кг - {args[0]}руб/кг\n\
Итого: {args[0] * args[1]}руб\n\
Внесено: {args[2]}руб\n\
Сдача: {args[2] - args[0] * args[1]}руб")


def main():
    name = input()
    price = int(input())
    weight = int(input())
    namber = int(input())
    handing_print(price, weight, namber, name)


if __name__ == '__main__':
    main()
