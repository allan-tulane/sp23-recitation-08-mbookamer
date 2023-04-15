
####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('book', 'back'), ('kookaburra', 'kookybird-'), ('relev-ant','-elephant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED={}):
    # TODO -  implement memoization
    #returns only the cost of edit distance 
    if (S, T) in MED_cache:
        return MED_cache[(S, T)] #if we already have it
    elif (T, S) in MED_cahce:
        return MED_cache[(T, S)] #if we already have it
    elif (S == ""):
        len(T) = MED_cache[(S, T)] #there is only one word, the other is empty
        return len(T)
    elif (T == ""):
        len(S) = MED_cache[(S, T)] #there is only one word, the other is empty
        return len(S)
    else:
        if (S[0] == T[0]): #if they are the same word
            MED_cache[(S, T)] = fast_MED(S[1:], T[1:])
            return MED_cache[(S, T)]
        else:
            MED_cache[(S, T)] = (1 + min(fast_MED(S, T[1:]), fast_MED(S[1:], T[1:])))
            return MED_cache[(S, T)]
    pass

def fast_align_MED(S, T, MED={}):
    # TODO - keep track of alignment
    def helper(S, T, MED_cache):
        #base case
        #same comments as before 
        if (S,T) in MED_cache:
            return MED_cache[(S, T)];
        elif (S == ""):
            MED_cache[(S, T)] = (len(T), "-" * len(T), T)
            return MED_cache[(S, T)]
        elif (T == ""):
            MED_cache[(S, T)] = (len(S), "-" * len(S), S)
            return MED_cache[(S, T)]
        elif (S == T): #same characters
            MED_cache[(S, T)] = (0, S, T)
            return MED_cache[(S, T)]
        else: #recursive step
            if (S[0] == T[0]): #if equal
                equal_step = helper(S[1:], T[1:], MED_cache)
                MED_cache[(S, T)] = (equal_step[0], S[0] + equal_step[1], T[0] + equal_step[2])
                return MED_cache[(S, T)]
            else: #if different 
                inset = helper(S, T[1:], MED_cache)
                delete = helper(S[1:], T, MED_cache)
                substitution = helper(S[1:], T[1:], MED_cahce)
                if min(insert[0], delete[0], substitution[0]) == substitution[0]:
                    MED_cache[(S, T)] = (substitution[0] + 1, S[0] + substitution[1], T[0] + substitution[2])
                    return MED_cache[(S, T)]
                elif min(insert[0], delete[0], substitution[0]) == delete[0]:
                    MED_cache[(S, T)] = (delete[0] + 1, S[0] + delete[1], "-" + delete[2])
                    return MED_cache[(S, T)]
                else:
                    MED_cache[(S, T)] = (insert[0] + 1, "-" + insert[1], T[0] + insert[2])
                    return MED_cache[(S, T)]
                
        
        res = helper(S, T, MED_cache)
        return res[1], res[2]
                                         
                
            
            
    pass

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])
