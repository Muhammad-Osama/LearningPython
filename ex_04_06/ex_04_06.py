def computepay(hours, rate):
    # print("In compute pay", hours, rate)
    if hours > 40:
        # print("Overtime")
        reg = rate * hours
        otp = (hours - 40) * (rate * 0.5)
        pay = reg + otp
    else:
        # print("Regular")
        pay = hours * rate
    # print("Returning", pay)
    return pay

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fr = float(sr)
fh = float(sh)

xp = computepay(fh, fr)

print("Pay", xp)
