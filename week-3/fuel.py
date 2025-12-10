while True:
    fraction = input("Fraction: ")
    a, b = fraction.rsplit("/")

    try: 
        x, y = map(int, (a, b))
        if x < 0:
            raise ValueError("Fraction must be positive.")
    except ValueError:
        print("Please enter a fraction with positive integers.")
        continue
    except ZeroDivisionError:
        print("Denominator must be greater than 0.")    
        continue
    if x > y:
        print("Numerator must be less than the denominator.")
        continue
    else:
        percentage = int(round(((x / y) * 100), 2))
        if percentage <= 1:
            print("E")
            break
        elif percentage >= 99:
            print("F")
            break
        else:
            print(f"{percentage}%")
            break
        
