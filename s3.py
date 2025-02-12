def palindrome(string):
    if string == string[:: -1]:
        return "it is palindrome"
    else:
        return "it is not palindrome"
n= input("enter the string")

print(palindrome("n"))

