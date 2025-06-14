import clib

# clib operations
print("Add 3 + 5 =", clib.add(3, 5))
print("Multiply 4 * 6 =", clib.multiply(4, 6))

# String operations
word = "father"
print("Reversed string:", clib.reverse_string(word))
print(f"Is '{word}' a palindrome?", clib.is_palindrome(word))
