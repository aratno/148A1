import math

sample_text = 'Subtract Squares is a two-player game. Below are the instructions:\n1. A positive whole number is picked randomly by the computer (we will call this the target).\n2. A player picks a perfect square to subtract from the target, and the difference becomes the new target.\n3. The next player picks a perfect square to subtract from the target, again producing a new target.\n4. Players alternate turns until there are no longer any perfect squares that can be subtracted from the target. Whomever is to play next when this happens loses.'

print('------------------SAMPLE TEXT------------------\n' + sample_text)

width = 110

#split sample text
split_text = sample_text.split('\n')

print('------------------SPLIT TEXT------------------\n' + str(split_text))

text_dict = {}
k = 0
for i in split_text:
    text_dict[k] = i
    k += 1
    
print('------------------DICTIONARY TEXT------------------\n' + str(text_dict))

#add line breaks to splitted text
for i in text_dict:
    if len(text_dict[i]) > width:
        split_text[i] = text_dict[i][:(len(text_dict[i]) - text_dict[i][::-1].find(' '))] + '\n' + text_dict[i][(len(text_dict[i]) - text_dict[i][::-1].find(' ')):]

#concatenate splitted text
final = ''
for i in split_text:
    final += i + '\n'

print('------------------FINAL TEXT------------------\n' + final)