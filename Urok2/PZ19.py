# Решение 19 задачи из хендбука

def Is_danger(x, y):
    rez = False
    if y <= 0:
        if x ** 2 / 4 + x / 2 - 35 / 4 <= y:
            rez = True
    elif -7 <= x <= -4:
        if 5 * x / 3 + 35 / 3 >= y:
            rez = True
    elif -4 <= x <= 0:
        if y <= 5:
            rez = True
    elif 0 <= x <= 5:
        if (x ** 2 + y ** 2) ** 0.5 <= 5:
            rez = True
    return rez


def bred(*args, **kwargs):
    if (args[0] ** 2 + args[1] ** 2) ** 0.5 > 10:
        print("Вы вышли в море и рискуете быть съеденным акулой!")
    elif Is_danger(args[0], args[1]):
        print("Опасность! Покиньте зону как можно скорее!")
    else:
        print("Зона безопасна. Продолжайте работу.")


def main():
    x = float(input())
    y = float(input())
    bred(x, y)


if __name__ == '__main__':
    main()
