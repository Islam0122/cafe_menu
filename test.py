''' a'''
def is_double_number(num):
    num_str = str(num)
    half_len = len(num_str) // 2
    return num_str[:half_len] == num_str[-half_len:]

def count_double_numbers(a, b):
    count = 0
    for num in range(a, b + 1):
        if is_double_number(num):
            count += 1
    return count

# Чтение входных данных
a = int( input('a='))
b = int( input('b='))

# Подсчет и вывод результата
result = count_double_numbers(a, b)
print(result)

''' b '''
def count_zeros_in_product(numbers):
    zero_count = 0
    min_power_of_5 = float('inf')

    for num in numbers:
        power_of_5 = 0
        while num % 5 == 0:
            power_of_5 += 1
            num //= 5

        zero_count += power_of_5
        min_power_of_5 = min(min_power_of_5, power_of_5)

    # Количество нулей равно минимальной степени 5 в разложении чисел
    return zero_count - min_power_of_5


# Чтение входных данных
N = int(input(f'Введите число N:'))
numbers = []

for i in range(N):
    num = int(input(f"Введите число {i + 1}: "))
    numbers.append(num)

# Подсчет и вывод результата
result = count_zeros_in_product(numbers)
print(result)
#c
# def min_additions_to_palindrome(s):
#     length = len(s)
#     additions = 0
#
#     for i in range(length // 2):
#         if s[i] != s[length - 1 - i]:
#             additions += 1
#
#     return additions
#
# # Чтение входных данных
# s = input()
#
# # Вызов функции и вывод результата
# result = min_additions_to_palindrome(s)
# print(result)
#d
def find_kth_sum_element(n, m, k, A, B):
    sums = []

    for i in range(n):
        for j in range(m):
            sums.append(A[i] + B[j])

    sums.sort()
    return sums[k - 1]

# Чтение входных данных
n, m, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Вызов функции и вывод результата
result = find_kth_sum_element(n, m, k, A, B)
print(result)
