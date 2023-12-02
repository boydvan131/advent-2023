import re

total = 0
numlist = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

with open("input.txt", "r") as input_file:
  for line in input_file:
    newline = ""
    for i in range(0, len(line)): 
      for x in range(0, len(line)):
        word = line[i:x]

        if word.isdigit():
          newline += word
        if word in numlist:
          newline += str(numlist[word])

    num = re.sub('\D', '', newline)
    total += int(num[0] + num[-1])

print(total)
