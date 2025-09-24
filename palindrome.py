word = str(input("enter your word")).lower()
if word.replace(" ","")== word.replace(" ","")[::-1]:
    print("palindrome")
else:
    print("not a palindrome")
