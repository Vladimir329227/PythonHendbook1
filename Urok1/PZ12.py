# Решение 12 задачи из хендбука


def summ(*args, **kwargs):
    s1 = args[0]
    s2 = args[1]
    if (len(s2) - len(s1)) > 0:
        s1 = (len(s2) - len(s1)) * "0" + s1
    elif (len(s1) - len(s2)) > 0:
        s2 = (len(s1) - len(s2)) * "0" + s2

    rez = ""

    for i in range(len(s1)):
        rez += str((int(s1[i]) + int(s2[i])) % 10)

    print(rez)


def main():
    namber_a = input()
    namber_b = input()
    summ(namber_a, namber_b)


if __name__ == '__main__':
    main()
