# Даны две переменные целого типа: A и B.
# Если их значения равны, то присвоить каждой переменной сумму этих значений,
# а если равны присвоить нулевые значения.
# Вывести новые значения переменных A и B.

# int check
income_values = {x: input(f"Enter {x} number: ") for x in ("A", "B")}
for key, value in income_values.items():
    current_value = value
    while type(current_value) != int:
        try:
            current_value = int(current_value)
        except ValueError:
            print(f"  (!) Your {key} input must be int-type")
            current_value = input(f"Input your {key} number: ")
    income_values[key] = current_value

# code
a, b = income_values.values()
a, b = (a + b, a + b) if a == b else (0, 0)
print(f"Answer | A = {a}, B = {b} |")
