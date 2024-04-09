# Check if a String contains Vowels in Python

vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

my_str = 'bobby'


if any(char in vowels for char in my_str):
    # 👇️ this runs
    print('The string contains at least one vowel')
else:
    print('The string does NOT contain any vowels')


print(any(char in vowels for char in 'hadz'))  # 👉️ True
print(any(char in vowels for char in 'hdz'))  # 👉️ False
print(any(char in vowels for char in ''))  # 👉️ False