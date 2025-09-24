# Logical Operators with Numbers

# 'and' returns the second operand if both are truthy.
# 10 is truthy (non-zero), 20 is also truthy, so Python returns 20.
print(10 and 20)  # Output: 20

# 'or' returns the first truthy operand it finds.
# 0 is falsy, so Python checks the next operand, 15, which is truthy.
print(0 or 15)    # Output: 15

# 'not' inverts the truth value.
# 25 is truthy (non-zero), so 'not 25' becomes False.
print(not 25)     # Output: False
