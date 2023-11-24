user_input = int(input("Enter an integer: "))

num=str(user_input)
first_digit = int(num[0])
last_digit = int(num[-1])

result = first_digit + last_digit

print("Sum of the first and last digit:", result)