import re

total = 0
with open("input.txt", "r") as input_file:
  for line in input_file:
    num = re.sub('\D', '', line)
    total += int(num[0] + num[-1])

print(total)