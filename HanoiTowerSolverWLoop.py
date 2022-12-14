# Solving Hanoi Tower with my algorithm
# This solves the most common problem (transport all disks from poles A to last poles)
import string
import itertools

def main():
    answer: tuple = []

    # input n of poles and disks
    input_allowed = False
    while not input_allowed:
        try: 
            n: int = int(input('Input number of poles and disks: '))
            n = max(0, n) # check so that no minus integer allowed
            input_allowed = True
        except:
            print('Please input valid integer!')

    # defining all possible alphabets
    max_alphabet_allowed = n
    alphabet = []
    for i, s in enumerate(iter_all_strings()):
        alphabet.append(s)
        if i == max_alphabet_allowed:
            break

    # get fixed number of poles
    # in this state poles are represented by ABC and disks are respresented by 123
    poles: tuple = tuple(alphabet[0:n])

    try:
        answer = hanoi_algorithm(poles)
    except:
        print('Sorry, cannot solve it')

    if answer:
        print('The answer is :', *answer, sep='\n')
        print('Hanoi Tower Solved! All disks moved to rightmost pole successfully.')
    else:
        print('Sorry invalid n poles!')
    
    

def hanoi_algorithm(poles: tuple) -> tuple:
    results = [] # container for the answers

    # raise error if less than 3 poles
    if len(poles) < 3:
        raise

    # move all disks in order from biggest (disk 1) to smallest (disk n)
    for i in reversed(list(poles)):
        results.append(['a', i])

    # pop last result because it itself doesn't have a meanign
    results.pop()

    # move the upmost right disk to the most left pole + 1
    results.append([poles[len(poles) - 1], poles[1]])

    # move the leftmost to the rightmost
    results.append([poles[0], poles[len(poles) - 1]])

    # move all possible disk to the rightmost
    for i in range(len(poles) - 2,  1, -1):
        results.append([poles[i], poles[len(poles) - 1]])

    # free the smallest disk and move all to the right destination
    results.append([poles[1], poles[0]])
    results.append([poles[1], poles[len(poles) - 1]])
    results.append([poles[0], poles[len(poles) - 1]])

    # return results
    return results

def iter_all_strings():
    # credits to https://stackoverflow.com/a/29351603
    for size in itertools.count(1):
        for s in itertools.product(string.ascii_lowercase, repeat=size):
            yield "".join(s)

if __name__ == '__main__':
    main()
