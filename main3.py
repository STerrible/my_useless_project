import itertools

def main(digits, operators):
    expression = f"{digits[0]} {operators[0]} {digits[1]} {operators[1]} {digits[2]} {operators[2]} {digits[3]}"    # индексирует кортежи
    try:
        result = eval(expression)   # использует арифметические операторы и цифры для получения ответа
        return result
    except (ZeroDivisionError, SyntaxError):    # для избежания портящих все ошибок
        return None


def find_solution(digits):
    permutation_of_digits = list(itertools.permutations(digits))    # переставляет введенные цифры каждый раз в новое положение
    permutation_of_operators = list(itertools.product(["+", "-", "*", "/"], repeat=3))  # ищет все возможные комбинации из 3 штук среди данных 4 операторов

    for ordered_digits in permutation_of_digits:
        for ordered_operators in permutation_of_operators:
            result = main(ordered_digits, ordered_operators)
            if result == 10 and result is not None:
                return ordered_digits, ordered_operators
    return None


input_digits = list(map(int, input("Enter 4 numbers: ").split()))

solution = find_solution(input_digits)

if solution:
    digits_order, operators_order = solution    # solution содержит в себе 2 кортежа
    print(
        f"Решение: {digits_order[0]} {operators_order[0]} {digits_order[1]} {operators_order[1]} {digits_order[2]} {operators_order[2]} {digits_order[3]} = 10")
else:
    print("Решение не найдено.")

