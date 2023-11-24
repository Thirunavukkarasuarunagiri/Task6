original_list = [10, 501, 22, 37, 100, 999, 87, 351]
def is_happy_number(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1

happy_numbers = [num for num in original_list if is_happy_number(num)]

print("Original List:", original_list)
print("Happy Numbers:", happy_numbers)
print("Number of Happy Numbers:", len(happy_numbers))