def timeConversion(s):
    time = s[-2:]
    hour = s[:2]
    if time == "PM" and hour != "12":
        s = str(12 + int(hour)) + s[2:]
    if time == "AM" and hour == "12":
        s = "00" + s[2:]
    return s[:-2]


print(timeConversion("12:01:00PM"))
