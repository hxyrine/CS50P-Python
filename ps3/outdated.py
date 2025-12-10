# Input M/D/Y format
# Convert to Y/M/D format

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date = input()
        date = date.replace("/", " ").split()
        m, d, y = [i.strip("/,") for i in date]
        if m.isdigit() and (int(m) <= len(months) - 1) and 0 < int(d) <= 31:
            print(f"{y}-{int(m):02}-{d:02}")
            break
        elif m.isalpha() and 0 < int(d) <= 31:
            print(f"{y}-{months.index(m) + 1:02}-{d}")
            break
        continue
    except ValueError:
        continue