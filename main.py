num = input("Введите числа через пробел: ").split()
# Создание нового списка с квадратами чисел
squares = [int(num)**2 for num in num]
# Вывод результата
print(squares)
