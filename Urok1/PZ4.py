# Решение 4 задачи из хендбука


def handing_print(*args, **kwargs):
    """Рассчет cдачи с покупки
       сдача покупки = получено денег - вес покупки * цена
       """
    weight = 2.5  # Вес покупки
    price = 38  # Цена покупки

    print(int(args[0] - weight * price))


def main():
    nammber = int(input())
    handing_print(nammber)


if __name__ == '__main__':
    main()
