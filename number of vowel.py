sentence = input("enter the sentence:").lower()

vowel = 0
consonent = 0

vowel_set = "a" "e" "i" "o" "u"

for char in sentence.lower():
    if char.isalpha():  # Check if it's a letter
        if char in vowel_set:
            vowel += 1
        else:
            consonent += 1
print("vowel are:",vowel)
print("consonent are:",consonent)
