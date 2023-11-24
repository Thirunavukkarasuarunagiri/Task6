my_list = [3, 5, 2, 7, 8, 2, 7, 3, 1]
def first_non_repeating_element(lst):
    frequency_dict = {}

    non_repeating_elements = []

    for element in lst:
        frequency_dict[element] = frequency_dict.get(element, 0) + 1
        if frequency_dict[element] == 1:
            non_repeating_elements.append(element)
        elif frequency_dict[element] == 2:
            non_repeating_elements.remove(element)

    if non_repeating_elements:
        return non_repeating_elements[0]
    else:
        return None

result = first_non_repeating_element(my_list)
print("First Non-Repeating Element:", result)
