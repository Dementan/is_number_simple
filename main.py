def is_number_simple():
    a = int(input("Введите любое число:"))
    sum_divisors = 0
    for i in range(1, a+1):
        if a % i == 0:
            sum_divisors = sum_divisors + i
    print(sum_divisors)
    if sum_divisors == a + 1:
            return "Число простое"
    else:
            return "Число не простое"

print(is_number_simple())

