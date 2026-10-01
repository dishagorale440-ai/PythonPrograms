def is_palindrome(number):
    original = number
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10

    return original == reverse


print(is_palindrome(121))