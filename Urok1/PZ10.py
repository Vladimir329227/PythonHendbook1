# Решение 10 задачи из хендбука


def print_info(*args, **kwargs):
    print(
        f"Группа №{args[1][0]}.\n\
{args[1][2]}. {args[0]}.\n\
Шкафчик: {args[1]}.\n\
Кроватка: {args[1][1]}.")


def main():
    name = input()
    namber_closet = input()
    print_info(name, namber_closet)


if __name__ == '__main__':
    main()
