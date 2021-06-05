fname = input('Enter file name: ')
fhand = open(fname)

# create dictionary of email-count key-value pairs
counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) < 1 :
        continue
    if words[0] != 'From' :
        continue
    email = words[1]
    counts[email] = counts.get(email, 0) + 1

# Who sent the most emails
maxCount = None
maxSender = None
for sender, count in counts.items():
    if maxCount is None or count > maxCount :
        maxSender = sender
        maxCount = count

print(maxSender, maxCount)
