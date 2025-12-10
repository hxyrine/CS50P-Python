groceries = []
while True: 
    try: 
        item = input().upper()
        groceries.append(item)
    except EOFError:
        unique = sorted(list(set(groceries)))
        for item in unique:
            count = groceries.count(item)
            print(f"{count} {item}")
        break