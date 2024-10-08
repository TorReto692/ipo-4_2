num = list(map(int, input("Введите числа через пробел: ").split()))
# Создание нового списка с квадратами чисел
squares = [num**2 for num in num]
# Вывод результата
print(squares)