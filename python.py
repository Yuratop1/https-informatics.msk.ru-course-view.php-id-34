# Первая задача
# a = int(input())
# b = int(input())
# print((a ** 2 + b ** 2) ** 0.5)

# Вторая задача
# a = int(input())
# print(f"The next number for the number {a} is {a + 1}.\nThe previous number for the number {a} is {a - 1}.")

# Третья задача
# a = int(input())
# b = int(input())
# print(b // a)

# Четвёртая задача
# a = int(input())
# b = int(input())
# print(b % a)

# Пятая задача
# s = 109
# v = int(input())
# t = int(input())
# print((t*v)%s)

# Шестая задача
# a = int(input())
# print(a % 10)

# Седьмая задача
# a = int(input())
# print(a//10)

# Восьмая задача
# a = int(input())
# print((a % 100 - a % 10)//10)

# Девятая задача
# a = int(input())
# a = str(a)
# b = 0
# for i in a:
#     b += int(i)
# print(b)

# Десятая задача
# a = int(input())
# print(a + 2 - (a % 2))

# # Одиннадцатая задача
# a = int(input())
# print((a // 60) % 24, a % 60)

# Двенадцатая задача
# a = int(input())
# print(f"{a//3600 % 24}:{str(a // 60 % 60).zfill(2)}:{str(a % 60).zfill(2)}")

# Тринадцатая задача
# a = int(input())
# b = int(input())
# c = a
# a = b
# b = c
# print(a, b)

# # Четырнадцатая задача
# a = int(input())
# a = a * 45 + (a // 2) * 5 + ((a + 1) // 2 - 1) * 15
# print(a // 60 + 9, a % 60)

# Пятнадцатая задача
# a = int(input())
# b = int(input())
# c = int(input())
# if b >= 10:
#     count = int(str(a) + str(b)) * c
# else:
#     count = int(str(a) + str(b).zfill(2)) * c
# print(count // 100, count % 100)

# Шестнадцатая задача
# h1 = int(input())
# m1 = int(input())
# s1 = int(input())
# h2 = int(input())
# m2 = int(input())
# s2 = int(input())
# all1 = h1 * 3600 + m1 * 60 + s1
# all2 = h2 * 3600 + m2 * 60 + s2
# print(abs(all1 - all2))

# # Семнадцатая задача
# U = int(input())
# S = int(input())
# print((U + S - 1) // U)

# Восемнадцатая задача
# n, k = int(input()), int(input())
# print((n - k % n) % n)

# Девятнадцатая задача
# S = int(input())
# U_plus = int(input())
# U_minus = int(input())
# if int((S - U_plus) / (U_plus - U_minus) + 1) == (S - U_plus) / (U_plus - U_minus) + 1:
#     print(int((S - U_plus) / (U_plus - U_minus) + 1))
# else:
#     print(int((S - U_plus) / (U_plus - U_minus) + 1) + 1)

# Двадцатая задача
# a = int(input())
# print((a % 10) * 10 + ((a // 10) % 10) - a // 100 + 1)

# Двадцать первая задача
# n = int(input())
# m = int(input())
# print((n % m) * (m % n) + 1)

# Двадцать вторая задача
# a = int(input())
# b = int(input())
# print((((a // b) * a) + ((b // a) * b)) // ((a // b) + (b // a)))