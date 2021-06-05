fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'clown.txt'
fhand = open(fname)

counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0)  + 1

# find the most frequent word and its count
maxWord = None
maxCount = None
for word, count in counts.items():
    if maxCount is None or count > maxCount:
        maxWord = word
        maxCount = count

print(maxWord, maxCount)
