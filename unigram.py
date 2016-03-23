import math

from question2 import question_list
# from question3 import question_list
trainFileName = "hw6-WSJ-1.tags"
testFileName = "hw6-WSJ-2.tags"

a = ['PRP$', 'VBG', 'VBD', 'VBN', 'POS', 'VBP', 'WDT', 'JJ', 'WP', 'VBZ', 'DT', 'RP', 'NN', ')', '(', ',', '.', 'TO', 'PRP', 'RB', ':', 'NNS', 'NNP', 'VB', 'WRB', 'CC', 'RBR', 'CD', 'EX', 'IN', 'MD', 'NNPS', 'JJS', 'JJR']


class QuestionNode:

    def __init__(self,question,level):
        self.split_question = question
        self.level=level
        self.left = None
        self.right = None
        self.LM = None

    def eval(self,trainlist,i,j):
        if self.LM != None:
            if trainlist[i][j] not in self.LM.hm:
                return 1.0
            else:
                return self.LM.hm[trainlist[i][j]]
        else:
            if self.split_question(trainlist[i],j):
                return self.left.eval(trainlist,i,j)
            else:
                return self.right.eval(trainlist,i,j)


class LM:
    def __init__(self,hm):
        self.hm = hm


def entropy(hm):
    res = 0
    for t in hm:
        res += -1 * hm[t] * math.log(hm[t],2)
    return res


def mutualInformation(corpuslist,count,hmwhole,yeslist,nolist):
    nw = count

    hm1 = buildUnigram(corpuslist,yeslist)
    hm2 = buildUnigram(corpuslist,nolist)

    n1 = len(yeslist)
    n2 = len(nolist)

    w1 = float(n1)/nw
    w2 = float(n2)/nw

    H = entropy(hmwhole)
    H1 = entropy(hm1)
    H2 = entropy(hm2)

    return [H - w1*H1 - w2*H2,hm1,hm2]


def split(corpusList,idxlist,question):
    yeslist = []
    nolist = []
    for (i,j) in idxlist:
        if question(corpusList[i],j):
            yeslist.append((i,j))
        else:
            nolist.append((i,j))

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

    for (i,j) in idxlist:
        t = corpuslist[i][j]
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
    idxlist = []
    lineNum = 0
    with open(filename) as f:
        for line in f:
            tokens = line.strip().split(" ")
            templist = []
            for t in xrange(len(tokens)):
                templist.append(tokens[t])
                idxlist.append((lineNum,t))
                count += 1
            trainlist.append(templist)
            lineNum += 1

    return [trainlist, count, idxlist]


def aloglikihood_unigram(trainlist,hm):
    trainaloglikihood = 0

    for pos in trainlist:
        trainaloglikihood += math.log(float(hm[pos]),2)

    trainaloglikihood /= len(trainlist)

    return trainaloglikihood


def aloglikihood(trainlist,count,root_question_node):
    all = 0.0
    for i in xrange(len(trainlist)):
        for j in xrange(len(trainlist[i])):
            prob = root_question_node.eval(trainlist,i,j)
            all += math.log(float(prob),2)

    all /= count
    return all

def perplexity(all):
    return math.pow(2,-1*all)

def find_max_mi_question(hm,trainlist,idxlist,count,questionlist):
    max_mi = float("-inf")
    max_mi_question = None
    max_mi_left_idx = None
    max_mi_right_idx = None
    max_mi_left_LM = None
    max_mi_right_LM = None

    for question in questionlist:
        yeslist,nolist = split(trainlist,idxlist,question)
        c = len(idxlist)
        mi,hm1,hm2 = mutualInformation(trainlist,c,hm,yeslist,nolist)
        if mi > max_mi:
            max_mi = mi
            max_mi_question = question
            max_mi_left_idx = yeslist
            max_mi_right_idx = nolist
            max_mi_left_LM = hm1
            max_mi_right_LM = hm2



    return [max_mi_question,max_mi_left_idx,max_mi_right_idx,max_mi_left_LM,max_mi_right_LM]

def find_top_mi_question(hm,trainlist,count,questionlist):
    max_mi = 0
    max_mi_question = None

    res = []

    for question in questionlist:
        yeslist,nolist = split(trainlist,idxlist,question)
        c = len(idxlist)
        mi,hm1,hm2 = mutualInformation(trainlist,c,hm,yeslist,nolist)

        res.append((mi,question))

    res.sort(reverse=True)
    avg = 0.0
    with open("sortfunction_cat2","w") as f:
        for (mi,question) in res:
            avg += float(mi)
            f.write(str(question) + " "+str(mi) + "\n")

    print "avg: ",avg/len(res)
    return max_mi_question


def build_tree_stump(hm,trainlist,count,split_question):
    yeslist,nolist = split(trainlist,split_question)

    return yeslist,nolist


def train_tree_model(corpus,idxlist,level):

    hm = buildUnigram(corpus,idxlist)

    traincount = len(idxlist)

    if level == 1:
        root_question_node = QuestionNode(None, level)
        root_question_node.LM = LM(hm)
        return root_question_node

    split_question,max_mi_left_idx,max_mi_right_idx,max_mi_left_LM,max_mi_right_LM = find_max_mi_question(hm,corpus,idxlist,traincount,question_list)

    root_question_node = QuestionNode(split_question, level)
    print "level ",level,split_question

    question_list.remove(split_question)

    if len(hm) <= 1:
        root_question_node.LM = LM(hm)
        return root_question_node

    lev = level - 1

    if len(question_list) > 0 and len(max_mi_left_idx) > 0:
        root_question_node.left = train_tree_model(corpus,max_mi_left_idx,lev)

    if len(question_list) > 0 and len(max_mi_right_idx) > 0:
        root_question_node.right = train_tree_model(corpus,max_mi_right_idx,lev)
    print len(max_mi_left_idx)
    print len(max_mi_right_idx)
    if len(max_mi_left_idx) == 0 or len(max_mi_right_idx) == 0:
        root_question_node.LM = LM(hm)


    question_list.append(split_question)
    return root_question_node


if __name__ == "__main__":
    hm = {}

    trainlist, traincount,idxlist = buildCorpus(trainFileName)

    hm = buildUnigram(trainlist,idxlist)
    # print hm
    # for t in hm:
    #     yeslist,nolist = split(trainlist,t,bigramcriteria)
    #     mi = mutualInformation(trainlist,hm,yeslist,nolist)
    #     print mi,"\t",t

    # find_max_mi_question(hm,trainlist,traincount,question_list)

    find_top_mi_question(hm,trainlist,traincount,question_list)


    # specify the tree layer here
    root_question_node = train_tree_model(trainlist,idxlist,2)

    testlist, testcount, idxlist = buildCorpus(testFileName)

    all = aloglikihood(trainlist,traincount,root_question_node)

    print "average log likelihood of train set: %s" %all
    print "perplexity of test set: %s" %perplexity(all)


    all = aloglikihood(testlist,testcount,root_question_node)

    print "average log likelihood of test set: %s" %all
    print "perplexity of test set: %s" %perplexity(all)

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




