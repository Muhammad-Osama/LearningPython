fname = input('Enter file name: ')
fhand = open(fname)
count = 0
tot = 0.0
for line in fhand:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    count = count + 1
    ipos = line.find(':')
    snum = line[ipos + 1:]
    fnum = float(snum)
    tot = tot + fnum
print('Average spam confidence: ', tot/count)
