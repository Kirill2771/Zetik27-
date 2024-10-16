weight = float(input("Введите вес боксёра в килограммах: "))
if weight <= 60:
    category = 1 
elif weight <= 64:
    category = 2 
elif weight <= 69:
    category = 3 
else:
    category = 4
print(f"Боксер относится к категории номер: {category}")
