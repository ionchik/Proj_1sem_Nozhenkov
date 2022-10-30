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


# 2. Дан целочисленный список размера N.
# Найти количество различных элементов в данном списке.

n_value = input_int_value("N")
a = get_list_with_length(n_value)
unique_items_number = len(set(a))
print(f"The number of unique items in {a} is: {unique_items_number}.")
