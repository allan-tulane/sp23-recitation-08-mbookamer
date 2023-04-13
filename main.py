
####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('book', 'back'), ('kookaburra', 'kookybird-'), ('relev-ant','-elephant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T[1:])))


def fast_MED(S, T, MED={}):
    # TODO -  implement memoization
    #returns only the cost of edit distance 
    if (S, T) in MED_cache:
        return MED_cache[(S, T)]
    elif (T, S) in MED_cahce:
        return MED_cache[(T, S)]
    elif (S == ""):
        len(T) = MED_cache[(S, T)]
        return len(T)
    elif (T == ""):
        len(S) = MED_cache[(S, T)]
        return len(S)
    else:
        if (S[0] == T[0]):
            MED_cache[(S, T)] = fast_MED(S[1:], T[1:])
            return MED_cache[(S, T)]
        else:
            MED_cache[(S, T)] = (1 + min(fast_MED(S, T[1:]), fast_MED(S[1:], T[1:])))
            return MED_cache[(S, T)]
    pass

def fast_align_MED(S, T, MED={}):
    # TODO - keep track of alignment
    pass

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])
