# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def list_easy_value(number):
    list1 = []
    for i in range(2, number):
        check = 0
        for j in range(2, i):
            if i % j == 0:
                check = 1
        if check == 0:
            list1.append(i)
    return list1

def find_prime_factors(number, easy_list):
    list1 = []
    for i in easy_list:
        if number / i == 1:
            list1.append((i))
            break
        else:
            while number % i == 0:
                list1.append(i)
                number /= i
    return list1

try:
    num = int(input('Введите число N: '))
    list1 = find_prime_factors(num, list_easy_value(num))
    print(f'{num} = ', end='')
    for i in range(len(list1)):
        if i == len(list1) - 1:
            print(list1[i])
        else:
            print(f'{list1[i]} *', end=' ')

except:
    print('Введите целое число!')