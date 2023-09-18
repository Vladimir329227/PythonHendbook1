# Решение 16 задачи из хендбука

def summ(*args, **kwargs):
    template = '{:.' + str(2) + 'f}'
    rez = (args[1] - args[0]) / args[2]
    print(template.format(rez))


def main():
    namber_a = int(input())
    namber_b = int(input())
    namber_c = int(input())
    summ(namber_a, namber_b, namber_c)


if __name__ == '__main__':
    main()
