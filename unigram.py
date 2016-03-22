import math
from question2 import question_list
trainFileName = "hw6-WSJ-1.tags"
testFileName = "hw6-WSJ-2.tags"



def entropy(hm):
    res = 0
    for t in hm:
        res += -1 * hm[t] * math.log(hm[t],2)
    return res


def mutualInformation(corpuslist,hmwhole,yeslist,nolist):
    nw = len(corpuslist)

    hm1 = buildUnigram(corpuslist,yeslist)
    hm2 = buildUnigram(corpuslist,nolist)

    n1 = len(yeslist)
    n2 = len(nolist)

    print n1

    print n2

    w1 = float(n1)/nw
    w2 = float(n2)/nw

    H = entropy(hmwhole)
    H1 = entropy(hm1)
    H2 = entropy(hm2)

    print H1
    print H2

    return H - w1*H1 - w2*H2


def split(corpusList,target,bigramcriteria):
    yeslist = []
    nolist = []
    for i in range(len(corpusList)):
        if bigramcriteria(corpusList,i,target):
            yeslist.append(i)
        else:
            nolist.append(i)

    return [yeslist,nolist]


def bigramcriteria(corpusList,i,target):
    if i == 0:
        return False
    if corpusList[i-1] == target:
        return True
    else:
        return False



def buildUnigram(corpuslist,idxlist):
    count = len(idxlist)
    hm = {}
    for i in idxlist:
        t = corpuslist[i]
        if t not in hm:
            hm[t] = 1.0
        else:
            hm[t] += 1.0

    for t in hm:
        hm[t] /= count

    return hm


def buildCorpus(filename):
    count = 0
    trainlist = []
    with open(filename) as f:
        for line in f:
            tokens = line.strip().split(" ")
            for t in tokens:
                trainlist.append(t)
                count +=1

    return [trainlist, count]




def aloglikihood(trainlist,hm):
    trainaloglikihood = 0

    for pos in trainlist:
        trainaloglikihood += math.log(float(hm[pos]),2)

    trainaloglikihood /= len(trainlist)

    return trainaloglikihood


def find_max_mi_question(hm,trainlist,questionlist):
    max_mi = 0
    max_mi_question = None

    for question in questionlist:
        yeslist,nolist = split(trainlist,t,question)
        mi = mutualInformation(trainlist,hm,yeslist,nolist)
        if mi > max_mi:
            max_mi = mi
            max_mi_question = question

    return max_mi_question

if __name__ == "__main__":
    hm = {}

    trainlist, traincount = buildCorpus(trainFileName)

    hm = buildUnigram(trainlist,range(traincount))

    # print hm

    for t in hm:
        yeslist,nolist = split(trainlist,t,bigramcriteria)
        mi = mutualInformation(trainlist,hm,yeslist,nolist)
        print mi,"\t",t


    # print hm
    #
    # trainaloglikihood = aloglikihood(trainlist,hm)
    #
    # print "average log likelihood of training set: %s" %trainaloglikihood
    #
    # print "perplexity of training set: %s" %math.pow(2,-1*trainaloglikihood)
    #
    # testlist, testcount = buildCorpus(testFileName)
    #
    # testaloglikihood = 0
    #
    # testaloglikihood = aloglikihood(testlist,hm)
    #
    # print "average log likelihood of training set: %s" %testaloglikihood
    #
    # print "perplexity of training set: %s" %math.pow(2,-1*testaloglikihood)




