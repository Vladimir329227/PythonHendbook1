# Решение 5 задачи из хендбука


def handing_print(*args, **kwargs):
    """Рассчет cдачи с покупки
       сдача покупки = получено денег - вес покупки * цена
       """

    print(int(args[2] - args[1] * args[0]))


def main():
    price = int(input())
    weight = int(input())
    namber = int(input())
    handing_print(price, weight, namber)


if __name__ == '__main__':
    main()
