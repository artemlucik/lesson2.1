# Вывести последнюю букву в слове
word = 'Архангельск'
print(f'Last letter: {word[-1]}')

# Вывести количество букв а в слове
word = 'Архангельск'
print(f'Amount of letters: {len(word)}')

# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
word_vowels = [w for w in word.lower() if w in vowels]
print(f'Vowels letters in word: {word_vowels}')

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(f'Amount of words: {len(sentence.split(" "))}')

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
first_letters = [l[0] for l in list(sentence.split(' '))]
for letter in first_letters:
	print(letter)

# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
words = [l for l in  list(sentence.split(' '))]
average = sum(len(word) for word in words)/len(words)
print(f'Average length: {average}')