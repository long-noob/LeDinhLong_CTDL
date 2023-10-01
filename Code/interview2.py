def is_palindrome(n):
    n = n.lower().replace(" ", "")
    
    start = 0
    end = len(n) - 1
    
    while start < end:
        if n[start] != n[end]:
            return False
        start += 1
        end -= 1
    
    return True


input_string = "madam"
result = is_palindrome(input_string)

if result:
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")

