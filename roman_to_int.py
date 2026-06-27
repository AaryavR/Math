def roman_to_int(rom):
    roman = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    num = 0 
    for i in range(0, len(rom) - 1):
        if roman[rom[i]] < roman[rom[i + 1]]:
            num -= roman[rom[i]]
        else:
            num += roman[rom[i]]
    print(num) 

roman_to_int("VIII")
roman_to_int("MDCLXVI")  