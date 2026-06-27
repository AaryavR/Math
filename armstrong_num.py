def is_armstrong_num(num):
    temp = num
    total_sum = 0

    power = len(str(num))
    
    while temp > 0:
        digit = temp % 10          
        total_sum += digit ** power 
        temp //= 10              

    if num == total_sum:
        return True
    else:
        return False

print(is_armstrong_num(153))
print(is_armstrong_num(123)) 