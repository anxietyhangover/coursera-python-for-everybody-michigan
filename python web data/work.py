import re
with open('regex_sum_190010.txt') as f:
    text =f.read().splitlines()
total =0
for line in text:
    numbers = map(int, re.findall('[0-9]+', line))
    total = total + sum(numbers)
print total