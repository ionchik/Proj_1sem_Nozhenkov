# Проверить истинность высказывания:
# "Среди трех данных чисел есть хотя бы одна пара совпадающих.

# int check
income_values = [input(f"Enter {x} number: ") for x in range(1, 4)]
for index, value in enumerate(income_values):
    current_value = value
    while type(current_value) != int:
        try:
            current_value = int(current_value)
        except ValueError:
            print(f"  (!) Your {index + 1} input must be int-type")
            current_value = input(f"Input your {index + 1} number: ")
    income_values[index] = current_value

# code
answer = "true statement" if len(set(income_values)) != 3 else "false statement"
print(f'For these values it is {answer}.')
