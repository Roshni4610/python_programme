while True:
    num = int(input("Enter a number (0 to exit): "))
    if num == 0:
        break
    power = len(str(num))
    total = sum(int(digit) ** power for digit in str(num))
    print(f'num---> {num}')
    print(f'power---> {power}')
    print(f'total---> {total}')
    if total == num:
        print("Armstrong Number\n")
    else:
        print("Not an Armstrong Number\n")
