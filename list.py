#Добавление элементов 

# appened():Добавляет элементы в конец списка.
my_list = [1, 2, 3]
my_list.append(4)  # my_list = [1, 2, 3, 4]

# insert
numbers = [1, 2, 3,]
numbers.insert(1, 10) # numbers = [1, 10, 2, 3]

# remove(): Удоляет первое вхождение элемента из списка.
numbers =[1, 2, 3, 2, 4]
numbers.remove(2)   # numbers = [1, 3, 2, 4]
# index(): Возвращаяет индекс первого вхождения элемента в списке.
fruits = ['яблоко', 'груша', 'апельсин']
index_pear = fruits.index('груша')  #index_peafr = 1

# sort(): Сортирует элементы из списка.
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()  # numbers = [1, 1, 2, 3, 4, 5, 9]

