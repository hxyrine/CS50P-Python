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
        date = input("Date: ").strip()
        if "/" in date:
            m, d, y = map(int, date.split("/"))  # If m is str, will produce ValueError; reprompt
            if (0 < m <= 12) and (0 < d <= 31):  # Ensures m is within 12 and d is within 31
                print(f"{y}-{m:02}-{d:02}")
                break
        elif "," in date:
            date = date.split(" ")
            m, d, y = [i.strip(",") for i in date]
            d, y = map(int, (d, y))
            if not m.isalpha():
                break
            if (0 < d <= 31):
                print(f"{y}-{months.index(m) + 1:02}-{d:02}")
                break
    except ValueError:
        continue

    # I feel like it's a bit crudely made but I tried 🥲
