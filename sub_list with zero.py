my_list = [4, 2, -3, 1, 6]
def has_sublist_with_zero_sum(lst):
    n = len(lst)

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += lst[j]
            if current_sum == 0:
                return True

    return False

result = has_sublist_with_zero_sum(my_list)
if result:
    print("There is a sub-list with zero sum.")
else:
    print("No sub-list with zero sum found.")