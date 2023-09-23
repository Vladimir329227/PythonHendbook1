# Решение 6 задачи из хендбука

def Is_visocosniy_year(*args, **kwargs):
    if args[0] % 400 == 0:
        print("YES")
    elif args[0] % 100 == 0:
        print("NO")
    elif args[0] % 4 == 0:
        print("YES")
    else:
        print("NO")


def main():
    year = int(input())
    Is_visocosniy_year(year)


if __name__ == '__main__':
    main()
