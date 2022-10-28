# 1. Вычислить число pi c заданной точностью d. Число d находится в интервале [1e-1, 1e-10]
# Пример:
# - при d = 0.001, pi = 3.141.
# Примечание:
# Использовать только итерационные алгоритмы вычисления числа pi. Любой на ваш выбор.

# Написать функцию, которая принимает аргумент: точность вычисления числа pi

# Возвращает:

# Вычисленное число pi
# Количество выполненных итераций
# Погрешность вычисления

# Пример вызова функции: - vallis(1e-4) -> (3.141392685883853, 3928, -0.00019996770594010727)

#я не понимаю:((((((






# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# def list_easy_value(number):
#     list1 = []
#     for i in range(2, number):
#         check = 0
#         for j in range(2, i):
#             if i % j == 0:
#                 check = 1
#         if check == 0:
#             list1.append(i)
#     return list1

# def find_prime_factors(number, easy_list):
#     list1 = []
#     for i in easy_list:
#         if number / i == 1:
#             list1.append((i))
#             break
#         else:
#             while number % i == 0:
#                 list1.append(i)
#                 number /= i
#     return list1

# try:
#     num = int(input('Введите число N: '))
#     list1 = find_prime_factors(num, list_easy_value(num))
#     print(f'{num} = ', end='')
#     for i in range(len(list1)):
#         if i == len(list1) - 1:
#             print(list1[i])
#         else:
#             print(f'{list1[i]} *', end=' ')

# except:
#     print('Введите целое число!')


#3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
#  элементов исходной последовательности.

# def create_list(size):
#     lst = []
#     for i in range(size):
#         lst.append(int(input(f'Введите {i + 1} число: ')))

#     return lst

# try:
#     size = int(input('Введите размер вашего списка: '))
#     lst = create_list(size)
#     print(f'\nИсходный список: {lst}')
#     new_list = list(set(lst))
#     print(f'\nCписок неповторяющихся элементов: {new_list}')

# except:
#     print('Введите число!')


# 4. Задана натуральная степень k. Сформировать случайным образом список
#  коэффициентов многочлена и записать в файл многочлен степени k.
# (0,100)

# import random

# def create_string_polyn(k):
#     sting = ''
#     for i in range(k + 1):
#         random_val = random.randint(0, 100)
#         if random_val != 0:
#             if i == k - 1:
#                 sting += f'({random_val} * x) + '
#             elif i == k:
#                 sting += f'{random_val}'
#             else:
#                 sting += f'({random_val} * x^{k - i}) + '
#     sting += f' = 0'
#     return sting

# try:
#     real_k = int(input('Введите натуральную степень k: '))
#     if real_k <= 0:
#         print('Введите натуральное число!')
#         exit()

#     result_string = create_string_polyn(real_k)
#     print(result_string)

#     f = open('polynom.txt', 'a')
#     f.writelines('\n' + result_string)
#     f.close()

# except:
#     print('Введите натуральное число!')

