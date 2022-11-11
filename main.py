array = []

#добавление своих данных в массив
amountElements = int(input('Сколько чисел вы хотите ввести?'))
print(f'Поочередно введите {amountElements} чисел')
for index in range(amountElements):
    numbers = int(input())
    array.append(numbers)

#пузырьковая сортировка массива
print(f'Исходный массив: \n{array}')

for x in range(len(array)):
    for j in range(len(array)-1):
        if array[j] > array[j+1]:
            temp = array[j+1]
            array[j+1] = array[j]
            array[j] = temp

print(f'Отсортированый массив: \n{array}')