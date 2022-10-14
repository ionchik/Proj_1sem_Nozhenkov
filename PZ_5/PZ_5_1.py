# Составить функцию решения задачи: из заданного числа вычли сумму его цифр. Из
# результата вновь вычли сумму его цифр и т. д. Через сколько таких действий
# получится нуль?

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


def solve_task(value: int):
    action_number = 0
    while value:
        digit_sum = sum([int(x) for x in str(value)])
        value -= digit_sum
        action_number += 1
    return action_number


if __name__ == "__main__":
    income_number = input_int_value()
    answer = solve_task(income_number)
    print(f"Result: {answer}")
