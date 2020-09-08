from . import periodicelements

symbols = periodicelements.get_elements()
symbols_low = [s.lower() for s in symbols]

class ElementalWord:
    """Processing a word so it can be matched to elements."""

    def __init__(self,word):
        self._make_sequences(word)

    def _make_sequences(self,word):
        """Initialize a sequences object using the word as a template."""
        self.sequences = []
        n = len(word)
        if n > 0:
            self._grow_sequence('',n)
        self.wordlist = [self._make_word_list(s,word) for s in self.sequences]

    def _grow_sequence(self,sequence,n):
        """Grow a sequences object until the desired length.
        
        A sequences object is recursively expanded with double (D) or
        single (S), until the length of the word is reached.
        """
        #TODO: add triple option for elements with 3 letters / make this length-agnostic
        #See code at the bottom of this script for the beginning of an idea for how to do this.
        if n == 1:
            sequence += 'S'
            self.sequences.append(sequence)
        else:
            # duplicate the sequence
            sequence1,sequence2 = sequence,sequence
            n1,n2 = n,n
            # add S to one, and D to the other; adjust the remaining n
            sequence1 += 'S'
            sequence2 += 'D'
            n1 -= 1
            n2 -= 2
            # decide how to proceed, based on remaining n
            if n1 > 0:
                self._grow_sequence(sequence1,n1)
            else:
                self.sequences.append(sequence1)
            if n2 > 0:
                self._grow_sequence(sequence2,n2)
            else:
                self.sequences.append(sequence2)      

    def _make_word_list(self,sequence,word):
        """Make a list of possible elements from a word.
        
        Based on the word and a possible way to split this word up
        in elements of 1 or 2 letters, generate a list of hypothetical elements.
        """
        # Ensure that the sequence and the word match 
        if sequence.count("S") + sequence.count("D") * 2 != len(word):
            raise ValueError("Length of sequence (in 'S' and 'D') and word do not match")
        wordlist = []
        index = 0
        for i in sequence:
            if i == 'D':
                wordlist.append(word[index:index+2])
                index += 2
            elif i == 'S':
                wordlist.append(word[index])
                index += 1
        return wordlist


def _score_wordlist(word):
    """Score a word list on how well it matches the periodic system"""
    sname = []
    score = 0
    for n in word:
        n = n.lower()
        if n in symbols_low:
            i = symbols_low.index(n)
            sym = symbols[i]
            score += len(sym)
        else:
            sym = ''
        sname.append(sym)
    return (sname,score)


def periodic_name(userword):
    """Generate a sequence of periodic elements from a word or sentence."""
    # split up into individual words
    sentence = userword.split()
    output = []
    # match each word with the periodic system
    for word in sentence:
        sequencer = ElementalWord(word)
        basescore = 0
        periodicname = []
        for word_sequence in sequencer.wordlist:
            sname,score = _score_wordlist(word_sequence)
            if score > basescore:
                periodicname = sname
                basescore = score
        output.append(periodicname)
    print("For", userword, "the closest periodic table sequence is:", output)



#TODO
# A much simpler, and length-agnostic way to go from a word to the word chopped up
# into a list of lists of elements.
# Unfortunately not yet functional, but a few good nights of sleep away?
#
# def word_to_list(word, n):
#     collection = []
#     while len(word) > 0:
#         subcollection = []
#         for i in range(n):
#             if len(word) > i:
#                 subcollection.append(word[:i+1])
#         collection.append(subcollection)
#         word = word[1:]
#     return(collection)
#
# Resulting in a matrix of the word, chopped up into pieces as follows
# Where a new column/first order of the list starts with a new letter
# And the second list order/row is populated by increasing size chunks of the word.
# [0][0]    [1][0]    [2][0]    [3][0] (...) [m][0]
# [0][1]    [1][1]    [2][1]    [3][1]     
# [0][2]    [1][2]    [2][2]    [3][2]
# (...)
# [0][n]    [1][n]    [2][n]    [3][n] (...)       
#
# In principle, sampling the next element for a matching word-list could be formulated:
# [wordlist_element[a][b], wordlist_element[a'][b], (...), wordlist_element[n][b]]
# Where b is all options from 1:n, and a' is the sum of a+b+1 from the previously selected element.
