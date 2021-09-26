# Для регистрации на сайте, пользователи часто вводят Имя и Фамилию с маленькой буквы.
# Напишите мини-программу, которая будет запрашивать у пользователя имя и фамилию
# и заменять первые буквы буквами в верхнем регистре.
# Измененные данные(имя и фамилию) вывести на экран.

name = input("Имя: ")
surname = input("Фамилия: ")

mistake = name[0]
mistake_true = mistake.upper()
true_name = name.replace(mistake, mistake_true)

mistake_s = surname[0]
mistake_true_s = mistake_s.upper()
true_surname = surname.replace(mistake_s, mistake_true_s)

print(true_name)
print(true_surname)
