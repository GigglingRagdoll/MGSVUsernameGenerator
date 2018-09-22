
import re

with open('words_simplified.txt', 'r') as f:
    words = re.sub('\s', ' ', f.read()).split(' ')

filtered_words = []
r = 1000

for i in range(len(words)):
    word = words[i]

    # hope radius is large enough to catch nearby words
    searchspace = words[i-r:i+r]

    if word == '':
        continue 

    # remove plurals
    elif word[:-1] in searchspace and word[-1] == 's':
        print(word)
        continue

    # also removes plurals
    elif word[:-2] in searchspace and word[-2:] == 'es':
        print(word)
        continue

    # removes more plurals
    elif (word[:-3] in searchspace or word[:-5] in searchspace) and word[-3:] == 'men':
        print(word)
        continue

    # removes ly words
    elif word[:-2] in searchspace and word[-2:] == 'ly':
        print(word)
        continue

    else:
        filtered_words.append(word)

with open('words_simplified.txt', 'w') as f:
    for word in filtered_words:
        f.write('{}\n'.format(word))