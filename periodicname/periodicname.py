import pandas

class Sequencer:
    """Processing a word so it can be matched to elements."""

    def __init__(self,word):
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
        #TODO: add triple option for elements with 3 letters
        if n == 1:
            sequence += 'S'
            self.sequences.append(sequence)
        else:
            # duplicate
            sequence1, sequence2 = sequence,sequence
            n1, n2 = n,n
            # alter
            sequence1 += 'S'
            sequence2 += 'D'
            n1 -= 1
            n2 -= 2
            # proceed
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
        in elements of 1, 2, or 3 letters, generate a list of hypothetical elements.
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

def get_elements():
    ps = pandas.read_csv('periodicname/data/periodicdata.csv')
    symbols = ps['symbol'].tolist()
    return symbols

class PeriodicElements:
    """Loading and processing the Periodic System."""
    symbols = get_elements()
    symbols_low = [s.lower() for s in symbols]

    def word_to_symbol(self, word):
        """Score a word list on how well it matches the periodic system"""
        sname = []
        score = 0
        for n in word:
            n = n.lower()
            if n in self.symbols_low:
                i = self.symbols_low.index(n)
                sym = self.symbols[i]
                score += len(sym)
            else:
                sym = ''
            sname.append(sym)
        return (sname,score)


def periodic_name(word):
    """Generate a sequence of periodic elements from a word."""
    sequencer = Sequencer(word)
    periodic = PeriodicElements() #TODO instantiate this only once
    basescore = 0
    periodicname = []
    for word_sequence in sequencer.wordlist:
        sname, score = periodic.word_to_symbol(word_sequence)
        if score > basescore:
            periodicname = sname
            basescore = score
    print("For the word", word, "the closest periodic table sequence is:", periodicname)

if __name__ == '__main__':
    periodic_name("Barbara")
    periodic_name("Otie")