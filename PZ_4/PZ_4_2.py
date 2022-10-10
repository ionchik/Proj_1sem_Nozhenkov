# Дано целое число N (> 0). Найти сумму 1^N + 2^N-1 + … + N^1.

# int check
incoming_value = input("Input your int number: ")
while type(incoming_value) != int:
    try:
        incoming_value = int(incoming_value)
    except ValueError:
        print("(!) Your input must be int-type.")
        incoming_value = input("Input your int number: ")

# code
answer = 0
for iteration in range(incoming_value):
    answer += (iteration + 1) ** (incoming_value - iteration)
print(f"Total amount: {answer}.")
