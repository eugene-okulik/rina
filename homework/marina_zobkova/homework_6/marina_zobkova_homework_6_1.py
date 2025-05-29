"""Assignment 1"""
import string

text = (
    'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
    'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
)
clean_text = text.translate(str.maketrans('', '', string.punctuation))
words = clean_text.split()
ing_words = []
for word in words:
    ing_words.append(word + 'ing')
print(' '.join(ing_words))
