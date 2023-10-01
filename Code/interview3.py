def reverse_integer(num):
    result = 0

    while num != 0:
        digit = num % 10
        result = result * 10 + digit
        num = num // 10

    return result

num = 292003
reversed_num = reverse_integer(num)
print(f"The reversed integer of {num} is {reversed_num}")