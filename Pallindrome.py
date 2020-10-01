str=str(input("Enter string to check Palindrome or not :"))
rev_str=reversed(str)
if list(str)==list(rev_str):
  print("Palindrome")
else:
  print("Not Palindrome")
