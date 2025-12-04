word=str(input("write the sentence")).lower()
new_word=word.replace(" ","").replace(";","").replace("@","").replace("#","").replace("$","")
vowel=0
consonet=0
vowel_word="aeiou"
for i in new_word:
    if i.isalpha():
        if i in vowel_word:
            vowel+=1
        else:
            consonet+=1
print(f"total number of vowels are:{vowel} and total number of consonet are{consonet}")