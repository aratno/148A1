sample_text = ['Welcome to [Game]', ['Line 1', 'Line 2', 'Line 3'], 'Thanks for playing.']

def print_in_box(width, title, alignment):
    """
    Output should have each element of the title into each box. Therefore, elements in title that are lists themselves (or [String].split([delim])) should be in the same box.
    """
    if alignment in ('C', 'L'):
        print('Alignment: ' + alignment)
        if alignment == 'C':
            pass #Work here.
        elif alignment == 'L':
            pass
        else:
            pass
    else:
        print('Alignment unknown.')

print_in_box(80, sample_text, 'C')
