name = 'Jennifer'

print(name[1:-1])

first = 'John'
last = 'Smith'

message = first + '[' + last + ' ] is a code '

msg = f'{first} [{last}] is a coder'
print(msg)

course = 'Python for Beginners'

print(course.upper())
print(course.lower())
print(course.find('P'))
print(course)

# 30 Days of Python - Day 4 (Strings) - Exercises cozumleri

# 1-2
print(' '.join(['Thirty', 'Days', 'Of', 'Python']))   # Thirty Days Of Python
print(' '.join(['Coding', 'For', 'All']))             # Coding For All

# 3-4
company = 'Coding For All'
print(company)

# 5
print(len(company))          # 14

# 6-7
print(company.upper())       # CODING FOR ALL
print(company.lower())       # coding for all

# 8
print(company.capitalize())  # Coding for all
print(company.title())       # Coding For All
print(company.swapcase())    # cODING fOR aLL

# 9 - ilk kelimeyi dilimle
print(company[:6])           # Coding
print(company.split()[0])    # alternatif

# 10 - 'Coding' iceriyor mu?
print('Coding' in company)   # True
print(company.find('Coding'))   # 0  (yoksa -1 doner)
print(company.index('Coding'))  # 0  (yoksa hata verir)

# 11 - 'Coding' -> 'Python'
print(company.replace('Coding', 'Python'))   # Python For All

# 12
print('Python for Everyone'.replace('Everyone', 'All'))   # Python for All

# 13
print(company.split())       # ['Coding', 'For', 'All']

# 14
print('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(', '))

# 15-17
print(company[0])            # C
print(len(company) - 1)      # 13  (son indeks)
print(repr(company[10]))     # ' '  (10. indeks bosluk!)

# 18-19 - akronim
print(''.join(w[0] for w in 'Python For Everyone'.split()))   # PFE
print(''.join(w[0] for w in company.split()))                 # CFA

# 20-21
print(company.index('C'))    # 0
print(company.index('F'))    # 7

# 22
print('Coding For All People'.rfind('l'))   # 19

# 23-27 - orijinal (Ingilizce) cumle
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))     # 31  (ilk gecis)
print(sentence.rindex('because'))   # 47  (son gecis)

phrase = 'because because because'
start = sentence.find(phrase)
print(sentence[start:start + len(phrase)])   # because because because

# 28-29
print(company.startswith('Coding'))   # True
print(company.endswith('coding'))     # False

# 30
print('   Coding For All      '.strip())   # Coding For All

# 31
print('30DaysOfPython'.isidentifier())         # False (rakamla basliyor)
print('thirty_days_of_python'.isidentifier())  # True

# 32
libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(libs))   # Django# Flask# Bottle# Pyramid# Falcon

# 33
print('I am enjoying this challenge.\nI just wonder what is next.')

# 34
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

# 35
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area:.0f} meters square.')

# 36
a, b = 8, 6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

