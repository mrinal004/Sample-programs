def is_matched(expression):
    mapping = dict(zip('({[', ')}]'))
    queue = []
    for letter in expression:
        if letter in mapping:
            queue.append(mapping[letter])
        elif letter not in mapping.values():
            raise ValueError('Unknown letter {letter}'.format(letter=letter))
        elif not (queue and letter == queue.pop()):
            return False
    return not queue
expression='{()}[]'
if is_matched(expression):
    print('balanced')
else:print('unbalanced')
    