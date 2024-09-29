import random
m = int(input("Введіть кількість слів: "))
n = int(input("Введіть кількість літер у словах: "))
ukrainian_alphabet = [
    'А', 'Б', 'В', 'Г', 'Ґ', 'Д', 'Е', 'Є', 'Ж', 'З', 'И', 'І', 'Ї', 'Й', 
    'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 
    'Ш', 'Щ', 'Ь', 'Ю', 'Я'
]
words = [''.join(random.choice(ukrainian_alphabet) for i in range(n)) for i in range(m)]
print(' '.join(words))