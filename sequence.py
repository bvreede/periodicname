import pandas


def sequencer(sequence,n):
    global sequences
    if n == 1:
        sequence += 'S'
        sequences.append(sequence)
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
            sequencer(sequence1,n1)
        else:
            sequences.append(sequence1)
        if n2 > 0:
            sequencer(sequence2,n2)
        else:
            sequences.append(sequence2)      


def start(word):
    n = len(word)
    if n > 0:
        sequencer('',n)
    else:
        sequences.append('')

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


def name_to_symbol(name):
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



if __name__ == '__main__':
    ## get the data and extract symbols
    ps = pandas.read_csv('periodicdata.csv')
    symbols = ps['symbol'].tolist()
    symlow = [s.lower() for s in symbols]
    
    names_to_test = ["Renato"]
    for name in names_to_test:
        sequences = []
        start(name)
        basescore = 0
        periodicname = []
        for s in sequences:
            namelist = makename(s,name)
            sname, score = name_to_symbol(namelist)
            if score > basescore:
                periodicname = sname
                basescore = score
        print("For the name", name, "the closest periodic table sequence is:", periodicname)