# Решение 8 задачи из хендбука

def Poisk(*args, **kwargs):
    if "зайка" in args[0]:
        print("YES")
    else:
        print("NO")


def main():
    text = input()
    Poisk(text)


if __name__ == '__main__':
    main()
