# Решение 15 задачи из хендбука


def summ(*args, **kwargs):
    minute = args[1] + args[2]
    hour = (args[0] + minute // 60) % 24
    minute %= 60
    hour = '0' * (2 - len(str(hour))) + str(hour)
    minute = '0' * (2 - len(str(minute))) + str(minute)
    print(f"{hour}:{minute}")


def main():
    namber_a = int(input())
    namber_b = int(input())
    namber_c = int(input())
    summ(namber_a, namber_b, namber_c)


if __name__ == '__main__':
    main()
