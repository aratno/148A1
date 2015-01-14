import string
import random

#This is a file to test out random functions

#width = int(input('Enter width: '))
#title = input('Enter title: ')
sample_list = random.sample(range(10), 4)
print(sample_list)

def print_in_box(width, title): #Make parameters 'width' and 'title' when removing user input
    #Make sure the longest element of 'title' can fit
    #Make it clearer that 'title' can be a list of strings

    #Check that the length of the longest element of 'title' is less than width
    if len(title) > width:
        print('ERROR: Title cannot fit in box of that width.')
    else:
        for i in title: #Find more descriptive name than 'i'
            for row in i.split('\n'):
                num_spaces = int((width - len(row))/2)  
                
                if row == i:
                    print('+' + '-' * width + '+')
                    if len(i) % 2 == 1:
                        print('|' + ' ' * num_spaces + i + ' ' * (num_spaces + 1) + '|')
                    else:
                        print('|' + ' ' * num_spaces + i + ' ' * num_spaces + '|')
                    print('+' + '-' * width + '+')
                else:
                    print('|' + ' ' * num_spaces + row + ' ' * (num_spaces) + '|') 
                #print('+' + '-' * width + '+') #Could be a useful method, draws single lines between rows and double lines between elements


def print_list(content): #Change name, no longer prints list
    #Edit param acceptance
    #output = [] #Only disabled for testing with 'output' as a string, not a list
    output = ''
    index = 0
    max_index = len(content)
    max_value = max(content)
    for i in content:
        index += 1
        output.append(' '*(len(str(max_index)) - len(str(index))) + str(index) + '. ' + ' '*(len(str(max_value)) - len(str(i))) + str(i))
    return output

print_in_box(80, ['Welcome to the game.', 'These are the rules:\n1. No bullying\n2. No being shit'])
