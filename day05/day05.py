names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']

print(names[2:4 ])

numbers = [2, 3, 4, 5, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)


matrix = [
    [1 , 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)
        
numbers = [5, 2, 1, 7, 4]
numbers.insert(2, 10)
print(numbers)

numberss = [5, 2, 1, 7, 4]
numberss.remove(2)
print(numberss)

#pop sondakini kaldırır , clear hepsini kaldırır.

#numbers = [5, 2, 1, 5, 7, 4]
#print(50 in numbers)

#count kaç kere geçtiğini söyler

#sort 
#reverse

#numbers2 = numbers.copy()

numbers = [2, 2, 4, 6, 3, 4, 6]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

list = []

list1 = [1, 2, 3, 4, 5]


print(list1[0:5:2])

mixed_data_types = ['Talat', 24, 1.83, 'Bekar', 'İstanbul']

it_companies = ['Facebook', 'Google']
it_companies.append('Amazon')
print(it_companies)

print(len(it_companies))

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
min_age = ages[0]
max_age = ages[-1]

print(ages)
print(min_age, max_age)

ages.append(min_age)
ages.append(max_age)
ages.sort()              # eklemeden sonra tekrar sırala
print(ages)  

n = len(ages)
mid = n // 2
if n % 2 == 0:
    median = (ages[mid - 1] + ages[mid]) / 2
else:
    median = ages[mid]
print(median)

average = sum(ages) / len(ages)
print(average)








