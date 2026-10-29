# 2. Gün: 30 Günlük Python Programlama

import math

# ---------------- Seviye 1 ----------------

first_name = 'Ahmet'
last_name = 'Yılmaz'
full_name = first_name + ' ' + last_name
country = 'Türkiye'
city = 'İstanbul'
age = 25
year = 2026
is_married = False
is_true = True
is_light_on = True

# Tek satırda birden fazla değişken
language, day, topic = 'Python', 2, 'Değişkenler'

# ---------------- Seviye 2 ----------------

# 1. type() ile veri türlerini kontrol etme
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(language), type(day), type(topic))

# 2. Adın uzunluğu
print(len(first_name))

# 3. Ad ve soyad uzunluğunu karşılaştırma
print(len(first_name) > len(last_name))
print(len(first_name) == len(last_name))

# 4. Sayıları tanımlama
num_one = 5
num_two = 4

# 5 - 11. Aritmetik işlemler
total = num_one + num_two
diff = num_one - num_two
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print('total:', total)
print('diff:', diff)
print('product:', product)
print('division:', division)
print('remainder:', remainder)
print('exp:', exp)
print('floor_division:', floor_division)

# 12. Daire (yarıçap 30 metre)
radius = 30
area_of_circle = math.pi * radius ** 2
circum_of_circle = 2 * math.pi * radius
print('Alan:', area_of_circle)
print('Çevre:', circum_of_circle)

# Kullanıcıdan yarıçap alıp alan hesaplama
radius = float(input('Yarıçapı girin: '))
area = math.pi * radius ** 2
print('Alan:', area)

# 13. Kullanıcıdan bilgi alma
first_name = input('Adınız: ')
last_name = input('Soyadınız: ')
country = input('Ülkeniz: ')
age = int(input('Yaşınız: '))
print(first_name, last_name, country, age)

# 14. Python'daki anahtar kelimeler
help('keywords')
