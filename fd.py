
text = str(input('Введите текст: '))
print(text[::-1])


n = int(input('Введите сумму: '))
if n >= 1000:
    value = n / 10
    value2 = n - value
    print(f'Сумма: {value2}')
if n < 1000:
    print(f'Сумма: {n}')
