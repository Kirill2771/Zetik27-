number = int(input("Введите число: "))
if number % 2 != 0:
    print("YES")
elif 2 <= number <= 5 and number % 2 == 0:
    print("NO")
elif 6 <= number <= 20 and number % 2 == 0:
    print("YES")
elif number > 20 and number % 2 == 0:
    print("NO")
