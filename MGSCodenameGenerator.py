
import re

from random import randint 

with open('animals_simplified.txt', 'r') as animal_file:
    text = animal_file.read()
    animals = text.split('\n')

with open('words_simplified.txt', 'r') as noun_file:
    nouns = re.sub('\s', ' ', noun_file.read()).split(' ')

noun = nouns[randint(0, len(nouns)-1)]
animal = animals[randint(0, len(animals)-1)]

print('Your code name is {} {}!'.format(noun.capitalize(), animal))