import random


def input_int_value(argument: str):
    # Int check
    while type(incoming_value := input(f"Input your {argument}-number: ")) != int:
        try:
            incoming_value = int(incoming_value)
        except ValueError:
            print("(!) Your input must be int-type.")
        else:
            return incoming_value


def get_list_with_length(n: int):
    return [random.randint(-10, 10) for _ in range(n)]


# 3. Дан список размера N, все элементы которого, кроме последнего, упорядочены по
# возрастанию. Сделать список упорядоченным, переместив последний элемент на
# новую позицию.

n_value = input_int_value("N")
*a, b = get_list_with_length(n_value)
c = sorted(a) + [b]
print(f"Sorted {c} is {sorted(c)}.")
