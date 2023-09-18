# Решение 17 задачи из хендбука

def function(*args, **kwargs):
    print(int(args[1], 2) + args[0])


def main():
    namber_a = int(input())
    namber_b = input()
    function(namber_a, namber_b)


if __name__ == '__main__':
    main()
