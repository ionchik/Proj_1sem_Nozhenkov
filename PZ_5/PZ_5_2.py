# Описать функцию shift_left 3(A, В, C), выполняющую левый циклический сдвиг:
# значение А переходит в С, значение С - в В, значение В - в А (А, В, С
# вещественные параметры, являющиеся одновременно входными и выходными). С
# помощью этой функции выполнить левый циклический сдвиг для двух данных
# наборов из трех чисел: (А1, В1, C1) и (А2, B2, C2).l

def input_int_value():
    incoming_value = input("Input your number: ")
    # Int check
    while type(incoming_value) != int:
        try:
            incoming_value = int(incoming_value)
        except ValueError:
            print("(!) Your input must be int-type.")
            incoming_value = input("Input your number: ")

    return incoming_value


def shift_left3(a_input: int, b_input: int, c_input: int):
    return b_input, c_input, a_input


if __name__ == "__main__":
    for index in range(1, 3):
        a, b, c = [input_int_value() for i in range(3)]
        a, b, c = shift_left3(a, b, c)
        print(f"{index} group: A={a}, B={b}, C={c}")
