sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fr = float(sr)
fh = float(sh)
if fh > 40:
    # print("Overtime")
    reg = fr * fh
    otp = (fh - 40) * (fr * 0.5)
    xp = reg + otp
else:
    # print("Regular")
    xp = fh * fr
print("Pay:", xp)
