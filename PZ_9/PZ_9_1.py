# Организовать словарь avto, содержащий 3 ключа (марки авто) и списки
# из трех моделей в качестве значений. Обеспечить отображение вторых моделей по
# каждому авто, всех моделей словаря.

avto = {"Audi": ["A3", "Q8", "Q5"], "Mercedes-Benz": ["AMG", "Maybach", "CLS"],
        "Tesla": ["Model 3", "Model X", "Model S"]}
print("\n".join(f"{mark} -> {b}" for mark, [a, b, *c] in avto.items()))
