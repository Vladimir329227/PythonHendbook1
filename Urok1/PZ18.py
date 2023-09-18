# Решение 18 задачи из хендбука

def function(*args, **kwargs):
    print(args[1] - int(args[0], 2))


def main():
    namber_a = input()
    namber_b = int(input())
    function(namber_a, namber_b)


if __name__ == '__main__':
    main()
