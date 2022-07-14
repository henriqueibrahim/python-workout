def hex_output():
    decimalNum = 0
    hexNum = input("Enter a hex number to convert: ")
    for power, digit in enumerate(reversed(hexNum)):
        decimalNum += int(digit, 16) * (16 ** power)
    print(decimalNum)

hex_output()
