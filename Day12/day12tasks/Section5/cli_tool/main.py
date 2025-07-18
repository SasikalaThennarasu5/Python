import sys
from utils import capitalize, word_count

if len(sys.argv) > 1:
    text = ' '.join(sys.argv[1:])
    print('Capitalized:', capitalize(text))
    print('Word count:', word_count(text))
else:
    print('Usage: python main.py <your text>')
