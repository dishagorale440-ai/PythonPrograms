def remove_duplicates(numbers):
    unique_numbers = []

    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)

    return unique_numbers


print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))