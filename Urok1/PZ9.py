# Решение 9 задачи из хендбука


def food_counting(*args, **kwargs):
    """Рассчет количества седенной колбосы
        количества седенной колбосы = время / 2 * количество детей
        """
    print(int(args[0] / 2 * args[1]))


def main():
    time = int(input())
    children = int(input())
    food_counting(time, children)


if __name__ == '__main__':
    main()
