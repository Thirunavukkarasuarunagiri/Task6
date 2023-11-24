sorted_list = [1, 3, 5, 7, 9, 11]
def find_minimum_element(sorted_list):
    if not sorted_list:
        return None
    else:
        return sorted_list[0]

result = find_minimum_element(sorted_list)
print("Minimum Element:", result)