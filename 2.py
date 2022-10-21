def recur_sum(n):
    if n <= 1:
        return n
    else:
        return n + recur_sum(n - 1)


num = int(input("Введіть кінець діапазону - "))
if num <= 0:
    print("Введіть натуральне число !")
else:
    print("Сума натуральних чисел ", recur_sum(num))