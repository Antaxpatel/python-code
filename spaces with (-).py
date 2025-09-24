s = str(input("enter your script:"))
if s.startswith(" ") or s.endswith(" "):
    s = s.strip()
n =  ""
for text in s:
    if text ==" ":
        
        n += "-"
    else:
        n += text 
print(n)