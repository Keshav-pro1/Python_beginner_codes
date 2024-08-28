#Program to show entered string is a palindrome
def palindrome(s):
  if (s ==s[::-1]):
    return "The string is a palindrome"
  else:
    return "the string is not a palindrome"
s=input("Enter a word:")
print(palindrome(s))
