# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_tiket(n):

    half1 = n//1000
    half2 = n%1000

    print(half1)
    print(half2)

    sum1 = half1//100 + half1%100//10 + half1%10
    sum2 = half2//100 + half2%100//10 + half2%10
    # print(sum1)       #проверка суммы 1
    # print(sum2)       #проверка суммы 2
    if sum2 == sum1:
        return ("Вы счастливчик!")
    else:
        return ("Лузер!")



print(lucky_ticket(301202))



# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
