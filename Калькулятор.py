def calc():
    operation = input('Выберите операцию (+, -, *, /, ^): ')
    num1 = float(input('Введите первое число: '))
    num2 = float(input('Введите второе число: '))
  
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    elif operation == '^':
        result = num1 ** num2
    else:
        print('Ошибка! Введите корректную операцию.')
        result = calc()
  
    print('Результат: ')
    print(result)
  
calc()