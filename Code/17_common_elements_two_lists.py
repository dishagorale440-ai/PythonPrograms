def common_elements(list1, list2):
    common = []

    for number in list1:
        if number in list2 and number not in common:
            common.append(number)

    return common


print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))