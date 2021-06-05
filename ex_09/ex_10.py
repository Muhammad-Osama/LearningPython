fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'clown.txt'
fhand = open(fname)

counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0)  + 1

temp = list()
for k, v in counts.items() :
    newTup = (v , k)
    temp.append(newTup)

temp = sorted(temp, reverse=True)
#print('Sorted', temp[:5])

for v, k in temp[:5] :
    print(k, v)
