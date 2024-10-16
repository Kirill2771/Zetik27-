age = int(input("Введите ваш возраст: "))
gender = input("Введите ваш пол (m для мужчина, f для женщина): ").lower()
if 10 <= age <= 15 and gender == 'f':
    print("YES")
else:
    print("NO")
