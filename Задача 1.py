f = open('transactions.txt', encoding='UTF-8') # Открываем файл transactions.txt
f1 = open('pack.csv', 'w') # Создаём файл pack.csv
s = [el.split('?') for el in f] # Создаём матрицу значений из файла
# Задаём начальные значения минимальной ценыи соотвествующего ей товара
min_cost = float('inf') 
min_item = '' 
f1.write('ItemDescription;CostPerItem\n') # Вписываем в pack.csv заголовки столбцов
for el in s: # Перебираем все строки матрицы
    if 'НАБОР' in el[4]: # Если в названии есть слово "набор"
        # то записываем название и цену в таблицу
        f1.write(el[4]) 
        f1.write(';') 
        f1.write(el[6])
        f1.write('\n')
        # и меняем значение минимальной цены
        min_cost = min(min_cost, float(el[6].replace(',', '.')))
        min_item = el[4]
f1.close() # Закрываем pack.csv
print(f'Самый дешевый товар в категории набор: {min_item}, цена такого товара составит: {min_cost}') # Выводим самый дешёвый товар и его цену
    
