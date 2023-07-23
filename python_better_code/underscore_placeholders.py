# In Python, the underscore character `_` can be used as a visual separator for large numbers to
# improve readability. In this case, `num1` is assigned the value `1_000_000_000`, which is equivalent
# to `1000000000`. Similarly, `num2` is assigned the value `1_000_000`, which is equivalent to `1000000`.
num1 = 1_000_000_000
num2 = 1_000_000
sum = num1+num2
print("Sum:",sum)
print("Sum:",f'{sum:,}')