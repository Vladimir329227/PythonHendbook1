# Решение 16 задачи из хендбука

def viner(*args, **kwargs):
    args[0].sort(key=lambda i: i[0], reverse=1)
    print(f"          {args[0][0][1]}          \n\
  {args[0][1][1]}  \n\
                  {args[0][2][1]}  \n\
   II      I      III   ")


def main():
    speed_p = [int(input()), "Петя"]
    speed_v = [int(input()), "Вася"]
    speed_t = [int(input()), "Толя"]

    viner([speed_p, speed_v, speed_t])


if __name__ == '__main__':
    main()
