# name = input('Введите имя: ')
# age = input('Введите возраст: ')
# a = (f"Привет {name}, тебе {age} лет.")
# print(a)

# Задача(Калькулятор):

num = int(input('Первое число: '))
operator = input("Выберите оператора (+, -, *, /):")
num2 = int(input('Второе число: '))
if operator == '+':
     value = num + num2
     print(f'Результат : {num} + {num2} = {value}')
elif operator == '-':
     value = num - num2
     print(f'Результат : {num} - {num2} = {value}')
elif operator == '*':
     value = num * num2
     print(f'Результат : {num} * {num2} = {value}')
elif operator == '/':
    value = num / num2
    print(f'Результат : {num}  / {num2} = {value}')







