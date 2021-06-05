fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
fhand = open(fname)

hours = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) < 1 :
        continue
    if words[0] != 'From' :
        continue
    time = words[5]
    splTime = time.split(':')
    hour = splTime[0]
    hours[hour] = hours.get(hour, 0) + 1

for k, v in sorted(hours.items()) :
    print(k, v)
