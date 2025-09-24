a = 5
b = 2
c = 3

# Expression: a + b * c
# Multiplication (*) has higher precedence than addition (+)
# So: b * c = 2 * 3 = 6, then a + 6 = 5 + 6 = 11

am=a + b * c
print("your result of a + b * c=",am)

# Expression: (a + b) * c
# Parentheses force addition first: a + b = 5 + 2 = 7
# Then: 7 * c = 7 * 3 = 21

amm=(a + b) * c
print("your result of (a + b) * c=",amm)

# Expression: a ** c ** b
# Exponentiation (**) is right-associative
# So: c ** b = 3 ** 2 = 9, then a ** 9 = 5 ** 9 = 1953125

ae=a ** c ** b
print("your result of a ** c ** b=",ae)

# Expression: (b ** c) ** b
# Parentheses force left-to-right evaluation
# First: b ** c = 2 ** 3 = 8, then 8 ** b = 8 ** 2 = 64

mm=(b ** c) ** b
print("your result of (b ** c) ** b=",mm)
