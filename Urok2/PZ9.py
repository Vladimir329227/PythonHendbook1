# Решение 9 задачи из хендбука

def Poisk(*args, **kwargs):
    args[0].sort(key=lambda i: i[0])
    print(args[0][0])


def main():
    name1 = input()
    name2 = input()
    name3 = input()
    Poisk([name1, name2, name3])


if __name__ == '__main__':
    main()
