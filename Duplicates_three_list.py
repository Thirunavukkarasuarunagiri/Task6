list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
list3 = [6, 7, 8, 9, 10]
def find_duplicates(list1, list2, list3):

    combined_list = list1 + list2 + list3

    frequency_dict = {}

    duplicates = []

    for element in combined_list:
        frequency_dict[element] = frequency_dict.get(element, 0) + 1

        if frequency_dict[element] == 2:
            duplicates.append(element)

    return duplicates


result = find_duplicates(list1, list2, list3)
print("Duplicates:", result)