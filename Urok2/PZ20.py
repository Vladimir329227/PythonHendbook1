# Решение 20 задачи из хендбука


def Poisk(*args, **kwargs):
    rez = []
    for i in args:
        if "зайка" in i:
            rez.append(i)
    print(min(rez), len(min(rez)))


def main():
    a = input()
    b = input()
    c = input()
    Poisk(a, b, c)


if __name__ == '__main__':
    main()
