dict = {
    'name': 'Akyl',
    'age': '29',
    'phone_number': '0702000000',
    'inn': '90546809580'
}



#keys(): Возвращает все ключи словаря.

my_dict = {'name': 'John', 'age': 25,  'city': 'New York'}
all_keys = my_dict.keys()    # all_keys = ['name', 'age', 'city']

#values(): Возвращает все значения словаря.

data = {'x': 10, 'y': 29, 'z': 28}
all_values = data.values()    # all_values = [10, 29, 28]

#items(): Возвращает все пары ключ-значения словаря в виде кортежей.

my_dicy = {'name': 'Alice', 'age': 30,}
all_items = my_dict.items()   # all_items = [('name', 'Alice'),('age', 30)]

#get: Возвращает значения по ключу; если кляч отсутствует, возвращает указанное по указанию.

person = {'name': 'Bob', 'age': 37}
age_person = person.get()  # age = 37
height = person.get......

