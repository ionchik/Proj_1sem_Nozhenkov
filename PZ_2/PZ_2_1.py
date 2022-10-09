# Вариант 19. Дано трехзначное число. В нем зачеркнули первую справа цифру и
# приписали ее слева. Вывести полученное число.

# int check
incoming_value = input("Input your three-digit number: ")
while type(incoming_value) != int:
    try:
        if len(incoming_value) != 3:
            raise ValueError()
        incoming_value = int(incoming_value)
    except ValueError:
        print("Your input must be three-digit number")
        incoming_value = input("Input your three-digit number: ")

# code
answer = incoming_value % 10 * 100 + incoming_value // 10
print(f'Your Answer: {answer}.')
