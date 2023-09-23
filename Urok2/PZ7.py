# Решение 7 задачи из хендбука

def Is_paliandrom(*args, **kwargs):
    base_text = args[0][::-1]
    if base_text == args[0]:
        print("YES")
    else:
        print("NO")


def main():
    text = input()
    Is_paliandrom(text)


if __name__ == '__main__':
    main()
