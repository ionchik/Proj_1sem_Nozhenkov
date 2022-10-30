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
    return [random.randint(0, 1) for _ in range(n)]


# 1. Дан список размера N и целые числа К и L (1 < K < L < N).
# Найти сумму элементов списка с номерами от К до L включительно.

n_value = input_int_value("N")
k_value = input_int_value("K")
l_value = input_int_value("L")
a = get_list_with_length(n_value)
answer = sum(a[k_value:l_value + 1])
print(f"The amount of {a} from {k_value} to {l_value} indexes is: {answer}.")
