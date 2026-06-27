def bin_to_dec(binary):
    decimal = 0
    power = 0
    for i in range(len(binary) - 1, -1, -1):
        decimal += int(binary[i]) * (2 ** power)
        power += 1
    print(decimal) 

bin_to_dec("10010101") 