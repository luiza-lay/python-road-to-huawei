







cities = ("Москва", "Казань", "Сочи")
print("Первый город:", cities[0])
print("Третий город:", cities[2])
#2
colors = ("красный", "синий", "зеленый")
second_color = colors[1]
print("Второй цвет:", second_color)
movies = ("Потомки солнца", "Винченцо", "Триггер", "Завтра")
second_movies = movies[0]
last_movies = movies[3]
print("Первый фильм:", second_movies)
print("Последний фильм:", last_movies)
#4
tuple_a = (1, 2)
tuple_b = (3, 4)
result = tuple_a + tuple_b
print("Результат:", result)
#5
part1 = ("а", "б", "в")
part2 = ("г", "д", "е")
full = part1 + part2
print("Полный кортеж:", full)
#6
num1 = (1, 2, 3, 4)
num2 = (5, 6, 7, 8)
result = num1 + num2
print("Сумма:", result)
#7
numbers = (5, 3, 5, 7, 5, 9)
count_five = numbers.count(5)
print("Пятерок:", count_five)
#8
letters = ("а", "б", "а", "в", "а", "г")
count_a = letters.count("а")
print("Буква 'а' встречается", count_a , "раза")
#9
student = (5, 4, 4, 5, 5, 3, 5)
count_five = student.count(5)
print("Пятерок:", count_five)
#10
matrix = ((1,2), (3,4), (5,6))
print("Элемент:", matrix[1][0])
#11
table = ((10, 20, 30), (40, 50, 60))
value = table[1][1]
print("Число 50:", value)
#12
points = ((10, 20), (30, 40), (50, 60))
x_first_point = points[0][0]
y_last_point = points[-1][1]
print(f"X-координата первой точки:",  x_first_point)
print(f"Y-координата последней точки:" , y_last_point)
#13
def get_positive(numbers):
    result = ()
    for n in numbers:
        if n > 0:
            result = result + (n,)
    return  result

nums = (- 2, 5, -1, 0, 3)
print("Положительные:", get_positive(nums))
#14
def get_negative(numbers):
    result = ()
    for n in numbers:
        if  n < 0:
            result = result + (n,)
    return result


nums = (-2, 5, -1, 0, 3)
print("Отрицательные:", get_negative(nums))
#15
def get_positive(numbers):
    result = ()
    for n in numbers:
        if n > 10:
            result = result + (n,)
    return result

nums = (1, 3, 6, 10, 25, 44)
print("Числа больше 10:", get_positive(nums))
#16
def count_types(data):
    strings = 0
    numbers = 0
    for item in data:
        if type(item) == str:
            strings += 1
        elif type(item) == int or type(item) == float:
            numbers += 1
    return strings, numbers


mixed = (1, "hello", 3.14, "world")
print("Строк и чисел:", count_types(mixed))


#17
def count_small_big(numbers):
    small = 0
    big = 0
    for n in numbers:
        if n < 50:
            small = small + 1
        else:
            big = big + 1
    return  small, big
nums = (30, 80, 20, 90, 40)
print("Меньше 50 и больше или равно 50:", count_small_big(nums))


#18
def  count_neg_pos(numbers):
    neg = 0
    pos = 0

    for n in numbers:
        if n < 0:
            neg += 1
        elif n > 0:
            pos += 1
    return (neg, pos)

nums = (-2, 6, -3, 1, -9, 13)
result = count_neg_pos(nums)
print("Отрицательные:", result[0])
print("Положительные:", result[1])





