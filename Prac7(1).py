word = input("Введіть слова розділені комами і/або пробілами: ")
spl = word.replace(",", " ").split()
print(spl)
longest = max(spl, key=len)
print("найдовше слово -", longest, ", довжина слова -", len(longest))
shortest = min(spl, key=len)
print("найкоротше слово -", shortest, ", довжина слова -", len(shortest))