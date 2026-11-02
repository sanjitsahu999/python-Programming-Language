text = input("Enter a string: ")

reverse = text[::-1]

if text.lower() == reverse.lower():
    print("Palindrome String")
else:
    print("Not a Palindrome String")
