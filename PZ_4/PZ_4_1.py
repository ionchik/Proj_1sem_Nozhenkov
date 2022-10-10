# Дано вещественное число Х и целое число N (> 0). Найти значение выражения X -
# X^3/(3!) + X^5/(5!) - … + (-1)^N-X^(2*N+1)/((2*N+1)!) (N! = 12 …N).

# int check
x = input("Input your X number: ")
while type(x) != float:
    try:
        x = float(x)
    except ValueError:
        print("(!) Your input must be float-type.")
        x = input("Input your X number: ")

# float check
n = input("Input your N number: ")
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("(!) Your input must be int-type.")
        n = input("Input your N number: ")

# code
answer = 0
for iteration in range(n):
    factorial = 1
    count = 2 * iteration + 1
    while count:
        factorial *= count
        count -= 1
    answer += ((-1) ** iteration) * (x ** (2 * iteration + 1) / factorial)
print(f"Total amount: {answer}.")
