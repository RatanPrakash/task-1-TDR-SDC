# Problem Set 4A


def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    returnList = []
    if len(sequence) <= 1:
        return [sequence]
    i = 0
    while i < len(sequence):
        sequence = list(sequence)
        sequence[0], sequence[i] = sequence[i], sequence[0]                   ##swapping the chars
        sequence = str("".join(sequence))
        
        returnList += [sequence[0] + letter for letter in get_permutations(sequence[1:])]           #recursion func
        
        sequence = list(sequence)
        sequence[0], sequence[i] = sequence[i], sequence[0]                   ##swapping the chars again
        sequence = str("".join(sequence))

        i += 1
        
    return list(set(returnList))

    

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

