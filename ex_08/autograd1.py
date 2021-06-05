fhand = open('romeo.txt')

list_of_words = []

for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) < 1:
        continue
    for word in words:
        if list_of_words == []:
            list_of_words.append(word)
        elif word not in list_of_words:
            list_of_words.append(word)
print(sorted(list_of_words))
