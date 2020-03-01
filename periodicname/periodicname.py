import pandas

class Sequencer:
    def __init__(self,word):
        self.sequences = []
        n = len(word)
        if n > 0:
            self._grow_sequence('',n)
        else:
            self.sequences.append('')

    def _grow_sequence(self,sequence,n):
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


def makename(sequence,name):
    # Ensure that the sequence and the name match 
    if sequence.count("S") + sequence.count("D") * 2 != len(name):
        raise ValueError("Length of sequence (in 'S' and 'D') and name do not match")
    namelist = []
    index = 0
    for i in sequence:
        if i == 'D':
            namelist.append(name[index:index+2])
            index += 2
        elif i == 'S':
            namelist.append(name[index])
            index += 1
    return(namelist)


def name_to_symbol(name, symbols, symlow):
    sname = []
    score = 0
    for n in name:
        n = n.lower()
        if n in symlow:
            i = symlow.index(n)
            sym = symbols[i]
            score += len(sym)
        else:
            sym = ''
        sname.append(sym)
    return(sname,score)

def periodic_name(name):
    sequencer = Sequencer(name)
    symbols, symlow = get_elements()
    basescore = 0
    periodicname = []
    for s in sequencer.sequences:
        namelist = makename(s,name)
        sname, score = name_to_symbol(namelist, symbols, symlow)
        if score > basescore:
            periodicname = sname
            basescore = score
    print("For the name", name, "the closest periodic table sequence is:", periodicname)

def get_elements():
    ps = pandas.read_csv('periodicname/data/periodicdata.csv')
    symbols = ps['symbol'].tolist()
    symlow = [s.lower() for s in symbols]
    return(symbols,symlow)

if __name__ == '__main__':
    periodic_name("Barbara")

        