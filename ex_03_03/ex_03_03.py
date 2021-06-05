scr = input("Enter score: ")
fscr = float(scr)
if fscr > 1:
    print("Error, score should be between 0 and 1")
elif fscr >= 0.9:
    print("A")
elif fscr >= 0.8:
    print("B")
elif fscr >= 0.7:
    print("C")
elif fscr >= 0.6:
    print("D")
elif fscr < 0.6:
    print("F")
