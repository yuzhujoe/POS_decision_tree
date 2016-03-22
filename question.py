def bigramisNN(corpus,i):
    if i == 0:
        return False
    if corpus[i-1] == "NN":
        return True
    else:
        return False


def bigramisWP(corpus,i):
    if i == 0:
        return False
    if corpus[i-1] == "NN":
        return True
    else:
        return False
