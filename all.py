import math

def calculate_logarithm(base, number):
    if base <= 0 or base == 1:
        raise ValueError("Основание должно быть больше 0 и не равно 1.")
    if number <= 0:
        raise ValueError("Число должно быть больше 0.")
    return math.log(number, base)

# Ввод данных
try:
    base = float(input("Введите основание логарифма (больше 0 и не равно 1): "))
    number = float(input("Введите число, для которого нужно вычислить логарифм (больше 0): "))
    
    log_result = calculate_logarithm(base, number)
    print(f"Логарифм числа {number} по основанию {base} равен: {log_result:.4f}")
except ValueError as e:
    print(f"Ошибка: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
