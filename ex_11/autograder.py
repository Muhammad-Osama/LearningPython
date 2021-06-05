import re

fhand = open('regex_sum_1235323.txt')

num = list()

for line in fhand:
    line = line.rstrip()
    num_str = re.findall('[0-9]+', line)
    if len(num_str) == 0:
        continue
    [num.append(int(str)) for str in num_str]

print('Number of numbers in text:', len(num))
print('Sum of numbers in text:', sum(num))
