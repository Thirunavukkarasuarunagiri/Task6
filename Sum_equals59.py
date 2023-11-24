my_list = [10, 20, 30, 9]
target_sum = 59
def find_triplet_with_sum(lst, target_sum):
    n = len(lst)

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if lst[i] + lst[j] + lst[k] == target_sum:
                    return [lst[i], lst[j], lst[k]]

    return None

result = find_triplet_with_sum(my_list, target_sum)
if result:
    print("Triplet with sum 59 found:",result)
else:
    print("No triplet found with sum ",target_sum)