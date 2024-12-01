def numeric(n):
    result = []
    num = 1

    while len(result) < n * (n + 1) // 2:  # используем формулу суммы арифметической прогрессии
        result.extend([num] * num)  # Добавляем число num в последовательность num раз
        num += 1

    print(result[:n * (n + 1) // 2])


if __name__ == '__main__':
    print("Введите цифру для вывода последовательности: ")
    user_choice = int(input('>>> '))
    numeric(user_choice)
