# Решение 17 задачи из хендбука

"""
Python наш, сущий в памяти!
да компилируется код Твой;
да приидет царствие Софта Твоего;
да будут действительны указатели Твои
и в ОЗУ, как на жестком диске;
массив наш насущный подавай нам на каждый день;
и прости нам варнинги наши,
как и мы избавляемся от ошибок наших;
и не введи нас в бесконечный цикл,
но избавь нас от винды.
Ибо Твое есть Царство и сила и слава во веки.
Энтер.
"""


def discriminant(*args, **kwargs):
    discr = args[1] * args[1] - 4 * args[0] * args[2]
    rez = [0, 0]
    template = '{:.' + str(2) + 'f}'
    if discr > 0:
        if args[0] != 0:
            rez[0] = (-args[1] + (discr ** 0.5)) / (2 * args[0])
            rez[1] = (-args[1] - (discr ** 0.5)) / (2 * args[0])
            rez.sort(key=lambda x: float(x))
            print(template.format(rez[0]), template.format(rez[1]))
        else:
            if args[1] != 0:
                print(template.format(-args[2] / args[1]))
            else:
                if args[2] == 0:
                    print("Infinite solutions")
                else:
                    print("No solution")
    elif discr == 0:
        if args[0] != 0:
            print(template.format(-args[1] / (args[0] * 2)))
        else:
            if args[1] != 0:
                print(template.format(-args[2] / args[1]))
            else:
                if args[2] == 0:
                    print("Infinite solutions")
                else:
                    print("No solution")
    else:
        print("No solution")


def main():
    a = float(input())
    b = float(input())
    c = float(input())
    discriminant(a, b, c)


if __name__ == '__main__':
    main()
