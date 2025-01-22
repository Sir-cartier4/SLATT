import math

def calculate_logarithm(base, number):
    if base <= 0 or base == 1:
        raise ValueError("Основание должно быть больше 0 и не равно 1.")
    if number <= 0:
        raise ValueError("Число должно быть больше 0.")
    return math.log(number, base)

def calculate_natural_logarithm(number):
    if number <= 0:
        raise ValueError("Число должно быть больше 0.")
    return math.log(number)

# Ввод данных
try:
    choice = input("Выберите тип логарифма (1 - обычный, 2 - натуральный): ")
    
    if choice == '1':
        base = float(input("Введите основание логарифма (больше 0 и не равно 1): "))
        number = float(input("Введите число, для которого нужно вычислить логарифм (больше 0): "))
        log_result = calculate_logarithm(base, number)
        print(f"Логарифм числа {number} по основанию {base} равен: {log_result:.4f}")
        
    elif choice == '2':
        number = float(input("Введите число, для которого нужно вычислить натуральный логарифм (больше 0): "))
        natural_log_result = calculate_natural_logarithm(number)
        print(f"Натуральный логарифм числа {number} равен: {natural_log_result:.4f}")
        
    else:
        print("Ошибка: Неверный выбор. Пожалуйста, выберите 1 или 2.")
        
except ValueError as e:
    print(f"Ошибка: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
