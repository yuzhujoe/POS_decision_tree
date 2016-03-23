def bigramis0(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == "PRP$":
        return True
    else:
        return False


def bigramis1(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == "VBG":
        return True
    else:
        return False


def bigramis2(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == "VBD":
        return True
    else:
        return False


def bigramis3(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == "VBN":
        return True
    else:
        return False


def bigramis4(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == "POS":
        return True
    else:
        return False


def bigramis5(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == "VBP":
        return True
    else:
        return False


def bigramis6(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == "WDT":
        return True
    else:
        return False


def bigramis7(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == "JJ":
        return True
    else:
        return False


def bigramis8(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == "WP":
        return True
    else:
        return False


def bigramis9(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == "VBZ":
        return True
    else:
        return False


def bigramis10(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == "DT":
        return True
    else:
        return False


def bigramis11(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == "RP":
        return True
    else:
        return False


def bigramis12(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == "NN":
        return True
    else:
        return False


def bigramis13(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == ")":
        return True
    else:
        return False


def bigramis14(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == "(":
        return True
    else:
        return False


def bigramis15(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == ",":
        return True
    else:
        return False


def bigramis16(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == ".":
        return True
    else:
        return False


def bigramis17(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == "TO":
        return True
    else:
        return False


def bigramis18(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == "PRP":
        return True
    else:
        return False


def bigramis19(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == "RB":
        return True
    else:
        return False


def bigramis20(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == ":":
        return True
    else:
        return False


def bigramis21(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == "NNS":
        return True
    else:
        return False


def bigramis22(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == "NNP":
        return True
    else:
        return False


def bigramis23(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == "VB":
        return True
    else:
        return False


def bigramis24(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == "WRB":
        return True
    else:
        return False


def bigramis25(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == "CC":
        return True
    else:
        return False


def bigramis26(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == "RBR":
        return True
    else:
        return False


def bigramis27(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == "CD":
        return True
    else:
        return False


def bigramis28(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == "EX":
        return True
    else:
        return False


def bigramis29(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == "IN":
        return True
    else:
        return False


def bigramis30(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == "MD":
        return True
    else:
        return False


def bigramis31(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == "NNPS":
        return True
    else:
        return False


def bigramis32(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == "JJS":
        return True
    else:
        return False


def bigramis33(corpus, i):
    if i == 0:
        return False
    if corpus[i - 1] == "JJR":
        return True
    else:
        return False


def trigramis0_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis0_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis0_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis0_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis0_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis0_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis0_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis0_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis0_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis0_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis0_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis0_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis0_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis0_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis0_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis0_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis0_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis0_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis0_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis0_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis0_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis0_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis0_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis0_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis0_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis0_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis0_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis0_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis0_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis0_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis0_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis0_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis0_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis0_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP$" or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis1_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis1_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis1_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis1_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis1_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis1_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis1_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis1_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis1_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis1_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis1_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis1_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis1_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis1_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis1_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis1_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis1_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis1_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis1_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis1_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis1_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis1_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis1_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis1_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis1_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis1_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis1_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis1_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis1_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis1_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis1_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis1_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis1_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis1_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBG" or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis2_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis2_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis2_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis2_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis2_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis2_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis2_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis2_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis2_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis2_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis2_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis2_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis2_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis2_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis2_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis2_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis2_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis2_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis2_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis2_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis2_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis2_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis2_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis2_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis2_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis2_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis2_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis2_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis2_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis2_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis2_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis2_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis2_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis2_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBD" or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis3_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis3_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis3_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis3_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis3_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis3_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis3_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis3_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis3_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis3_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis3_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis3_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis3_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis3_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis3_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis3_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis3_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis3_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis3_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis3_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis3_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis3_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis3_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis3_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis3_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis3_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis3_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis3_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis3_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis3_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis3_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis3_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis3_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis3_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBN" or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis4_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis4_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis4_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis4_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis4_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis4_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis4_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis4_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis4_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis4_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis4_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis4_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis4_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis4_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis4_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis4_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis4_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis4_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis4_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis4_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis4_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis4_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis4_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis4_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis4_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis4_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis4_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis4_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis4_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis4_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis4_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis4_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis4_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis4_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "POS" or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis5_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis5_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis5_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis5_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis5_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis5_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis5_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis5_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis5_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis5_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis5_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis5_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis5_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis5_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis5_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis5_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis5_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis5_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis5_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis5_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis5_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis5_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis5_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis5_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis5_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis5_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis5_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis5_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis5_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis5_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis5_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis5_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis5_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis5_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBP" or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis6_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis6_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis6_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis6_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis6_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis6_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis6_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis6_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis6_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis6_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis6_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis6_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis6_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis6_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis6_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis6_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis6_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis6_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis6_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis6_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis6_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis6_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis6_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis6_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis6_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis6_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis6_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis6_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis6_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis6_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis6_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis6_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis6_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis6_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WDT" or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis7_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis7_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis7_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis7_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis7_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis7_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis7_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis7_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis7_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis7_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis7_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis7_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis7_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis7_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis7_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis7_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis7_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis7_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis7_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis7_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis7_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis7_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis7_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis7_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis7_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis7_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis7_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis7_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis7_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis7_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis7_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis7_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis7_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis7_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJ" or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis8_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis8_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis8_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis8_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis8_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis8_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis8_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis8_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis8_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis8_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis8_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis8_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis8_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis8_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis8_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis8_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis8_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis8_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis8_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis8_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis8_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis8_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis8_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis8_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis8_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis8_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis8_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis8_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis8_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis8_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis8_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis8_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis8_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis8_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WP" or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis9_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis9_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis9_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis9_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis9_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis9_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis9_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis9_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis9_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis9_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis9_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis9_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis9_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis9_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis9_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis9_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis9_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis9_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis9_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis9_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis9_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis9_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis9_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis9_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis9_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis9_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis9_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis9_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis9_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis9_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis9_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis9_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis9_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis9_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VBZ" or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis10_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis10_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis10_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis10_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis10_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis10_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis10_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis10_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis10_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis10_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis10_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis10_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis10_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis10_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis10_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis10_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis10_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis10_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis10_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis10_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis10_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis10_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis10_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis10_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis10_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis10_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis10_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis10_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis10_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis10_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis10_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis10_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis10_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis10_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "DT" or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis11_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis11_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis11_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis11_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis11_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis11_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis11_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis11_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis11_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis11_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis11_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis11_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis11_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis11_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis11_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis11_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis11_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis11_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis11_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis11_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis11_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis11_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis11_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis11_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis11_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis11_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis11_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis11_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis11_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis11_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis11_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis11_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis11_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis11_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RP" or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis12_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis12_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis12_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis12_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis12_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis12_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis12_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis12_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis12_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis12_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis12_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis12_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis12_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis12_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis12_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis12_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis12_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis12_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis12_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis12_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis12_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis12_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis12_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis12_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis12_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis12_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis12_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis12_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis12_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis12_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis12_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis12_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis12_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis12_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NN" or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis13_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis13_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis13_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis13_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis13_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis13_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis13_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis13_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis13_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis13_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis13_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis13_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis13_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis13_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis13_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis13_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis13_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis13_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis13_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis13_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis13_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis13_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis13_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis13_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis13_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis13_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis13_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis13_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis13_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis13_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis13_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis13_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis13_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis13_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ")" or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis14_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis14_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis14_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis14_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis14_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis14_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis14_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis14_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis14_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis14_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis14_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis14_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis14_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis14_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis14_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis14_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis14_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis14_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis14_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis14_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis14_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis14_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis14_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis14_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis14_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis14_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis14_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis14_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis14_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis14_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis14_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis14_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis14_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis14_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "(" or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis15_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis15_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis15_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis15_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis15_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis15_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis15_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis15_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis15_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis15_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis15_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis15_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis15_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis15_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis15_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis15_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis15_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis15_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis15_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis15_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis15_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis15_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis15_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis15_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis15_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis15_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis15_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis15_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis15_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis15_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis15_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis15_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis15_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis15_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "," or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis16_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis16_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis16_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis16_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis16_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis16_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis16_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis16_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis16_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis16_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis16_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis16_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis16_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis16_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis16_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis16_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis16_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis16_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis16_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis16_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis16_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis16_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis16_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis16_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis16_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis16_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis16_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis16_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis16_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis16_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis16_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis16_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis16_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis16_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "." or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis17_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis17_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis17_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis17_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis17_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis17_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis17_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis17_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis17_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis17_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis17_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis17_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis17_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis17_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis17_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis17_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis17_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis17_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis17_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis17_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis17_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis17_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis17_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis17_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis17_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis17_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis17_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis17_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis17_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis17_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis17_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis17_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis17_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis17_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "TO" or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis18_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis18_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis18_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis18_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis18_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis18_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis18_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis18_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis18_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis18_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis18_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis18_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis18_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis18_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis18_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis18_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis18_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis18_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis18_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis18_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis18_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis18_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis18_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis18_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis18_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis18_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis18_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis18_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis18_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis18_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis18_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis18_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis18_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis18_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "PRP" or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis19_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis19_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis19_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis19_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis19_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis19_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis19_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis19_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis19_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis19_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis19_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis19_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis19_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis19_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis19_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis19_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis19_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis19_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis19_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis19_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis19_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis19_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis19_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis19_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis19_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis19_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis19_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis19_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis19_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis19_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis19_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis19_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis19_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis19_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RB" or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis20_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis20_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis20_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis20_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis20_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis20_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis20_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis20_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis20_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis20_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis20_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis20_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis20_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis20_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis20_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis20_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis20_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis20_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis20_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis20_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis20_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis20_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis20_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis20_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis20_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis20_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis20_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis20_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis20_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis20_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis20_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis20_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis20_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis20_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == ":" or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis21_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis21_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis21_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis21_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis21_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis21_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis21_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis21_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis21_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis21_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis21_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis21_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis21_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis21_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis21_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis21_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis21_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis21_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis21_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis21_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis21_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis21_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis21_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis21_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis21_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis21_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis21_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis21_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis21_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis21_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis21_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis21_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis21_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis21_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNS" or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis22_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis22_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis22_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis22_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis22_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis22_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis22_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis22_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis22_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis22_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis22_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis22_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis22_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis22_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis22_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis22_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis22_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis22_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis22_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis22_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis22_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis22_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis22_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis22_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis22_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis22_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis22_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis22_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis22_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis22_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis22_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis22_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis22_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis22_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNP" or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis23_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis23_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis23_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis23_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis23_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis23_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis23_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis23_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis23_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis23_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis23_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis23_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis23_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis23_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis23_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis23_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis23_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis23_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis23_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis23_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis23_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis23_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis23_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis23_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis23_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis23_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis23_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis23_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis23_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis23_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis23_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis23_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis23_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis23_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "VB" or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis24_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis24_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis24_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis24_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis24_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis24_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis24_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis24_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis24_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis24_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis24_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis24_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis24_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis24_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis24_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis24_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis24_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis24_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis24_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis24_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis24_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis24_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis24_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis24_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis24_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis24_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis24_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis24_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis24_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis24_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis24_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis24_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis24_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis24_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "WRB" or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis25_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis25_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis25_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis25_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis25_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis25_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis25_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis25_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis25_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis25_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis25_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis25_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis25_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis25_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis25_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis25_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis25_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis25_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis25_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis25_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis25_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis25_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis25_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis25_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis25_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis25_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis25_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis25_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis25_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis25_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis25_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis25_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis25_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis25_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CC" or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis26_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis26_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis26_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis26_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis26_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis26_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis26_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis26_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis26_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis26_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis26_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis26_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis26_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis26_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis26_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis26_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis26_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis26_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis26_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis26_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis26_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis26_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis26_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis26_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis26_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis26_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis26_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis26_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis26_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis26_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis26_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis26_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis26_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis26_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "RBR" or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis27_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis27_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis27_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis27_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis27_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis27_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis27_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis27_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis27_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis27_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis27_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis27_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis27_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis27_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis27_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis27_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis27_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis27_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis27_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis27_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis27_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis27_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis27_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis27_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis27_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis27_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis27_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis27_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis27_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis27_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis27_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis27_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis27_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis27_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "CD" or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis28_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis28_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis28_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis28_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis28_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis28_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis28_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis28_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis28_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis28_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis28_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis28_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis28_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis28_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis28_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis28_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis28_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis28_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis28_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis28_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis28_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis28_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis28_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis28_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis28_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis28_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis28_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis28_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis28_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis28_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis28_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis28_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis28_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis28_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "EX" or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis29_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis29_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis29_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis29_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis29_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis29_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis29_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis29_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis29_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis29_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis29_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis29_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis29_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis29_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis29_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis29_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis29_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis29_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis29_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis29_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis29_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis29_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis29_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis29_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis29_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis29_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis29_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis29_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis29_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis29_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis29_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis29_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis29_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis29_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "IN" or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis30_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis30_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis30_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis30_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis30_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis30_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis30_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis30_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis30_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis30_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis30_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis30_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis30_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis30_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis30_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis30_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis30_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis30_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis30_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis30_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis30_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis30_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis30_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis30_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis30_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis30_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis30_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis30_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis30_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis30_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis30_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis30_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis30_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis30_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "MD" or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis31_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis31_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis31_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis31_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis31_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis31_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis31_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis31_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis31_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis31_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis31_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis31_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis31_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis31_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis31_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis31_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis31_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis31_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis31_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis31_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis31_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis31_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis31_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis31_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis31_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis31_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis31_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis31_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis31_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis31_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis31_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis31_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis31_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis31_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "NNPS" or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis32_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis32_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis32_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis32_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis32_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis32_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis32_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis32_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis32_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis32_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis32_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis32_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis32_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis32_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis32_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis32_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis32_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis32_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis32_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis32_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis32_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis32_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis32_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis32_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis32_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis32_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis32_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis32_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis32_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis32_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis32_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis32_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis32_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis32_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJS" or corpus[i - 2] == "JJR":
        return True
    else:
        return False


def trigramis33_0(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == "PRP$":
        return True
    else:
        return False


def trigramis33_1(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == "VBG":
        return True
    else:
        return False


def trigramis33_2(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == "VBD":
        return True
    else:
        return False


def trigramis33_3(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == "VBN":
        return True
    else:
        return False


def trigramis33_4(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == "POS":
        return True
    else:
        return False


def trigramis33_5(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == "VBP":
        return True
    else:
        return False


def trigramis33_6(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == "WDT":
        return True
    else:
        return False


def trigramis33_7(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == "JJ":
        return True
    else:
        return False


def trigramis33_8(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == "WP":
        return True
    else:
        return False


def trigramis33_9(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == "VBZ":
        return True
    else:
        return False


def trigramis33_10(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == "DT":
        return True
    else:
        return False


def trigramis33_11(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == "RP":
        return True
    else:
        return False


def trigramis33_12(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == "NN":
        return True
    else:
        return False


def trigramis33_13(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == ")":
        return True
    else:
        return False


def trigramis33_14(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == "(":
        return True
    else:
        return False


def trigramis33_15(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == ",":
        return True
    else:
        return False


def trigramis33_16(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == ".":
        return True
    else:
        return False


def trigramis33_17(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == "TO":
        return True
    else:
        return False


def trigramis33_18(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == "PRP":
        return True
    else:
        return False


def trigramis33_19(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == "RB":
        return True
    else:
        return False


def trigramis33_20(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == ":":
        return True
    else:
        return False


def trigramis33_21(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == "NNS":
        return True
    else:
        return False


def trigramis33_22(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == "NNP":
        return True
    else:
        return False


def trigramis33_23(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == "VB":
        return True
    else:
        return False


def trigramis33_24(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == "WRB":
        return True
    else:
        return False


def trigramis33_25(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == "CC":
        return True
    else:
        return False


def trigramis33_26(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == "RBR":
        return True
    else:
        return False


def trigramis33_27(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == "CD":
        return True
    else:
        return False


def trigramis33_28(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == "EX":
        return True
    else:
        return False


def trigramis33_29(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == "IN":
        return True
    else:
        return False


def trigramis33_30(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == "MD":
        return True
    else:
        return False


def trigramis33_31(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == "NNPS":
        return True
    else:
        return False


def trigramis33_32(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == "JJS":
        return True
    else:
        return False


def trigramis33_33(corpus, i):
    if i == 0 or i == 1:
        return False
    if corpus[i - 1] == "JJR" or corpus[i - 2] == "JJR":
        return True
    else:
        return False

def isPunctuation1(corpus,i):
    if i == 0:
        return False
    if corpus[i-1] in b1:
        return True
    else:
        return False


question_list = [
    trigramis0_0,
    trigramis0_1,
    trigramis0_2,
    trigramis0_3,
    trigramis0_4,
    trigramis0_5,
    trigramis0_6,
    trigramis0_7,
    trigramis0_8,
    trigramis0_9,
    trigramis0_10,
    trigramis0_11,
    trigramis0_12,
    trigramis0_13,
    trigramis0_14,
    trigramis0_15,
    trigramis0_16,
    trigramis0_17,
    trigramis0_18,
    trigramis0_19,
    trigramis0_20,
    trigramis0_21,
    trigramis0_22,
    trigramis0_23,
    trigramis0_24,
    trigramis0_25,
    trigramis0_26,
    trigramis0_27,
    trigramis0_28,
    trigramis0_29,
    trigramis0_30,
    trigramis0_31,
    trigramis0_32,
    trigramis0_33,
    trigramis1_0,
    trigramis1_1,
    trigramis1_2,
    trigramis1_3,
    trigramis1_4,
    trigramis1_5,
    trigramis1_6,
    trigramis1_7,
    trigramis1_8,
    trigramis1_9,
    trigramis1_10,
    trigramis1_11,
    trigramis1_12,
    trigramis1_13,
    trigramis1_14,
    trigramis1_15,
    trigramis1_16,
    trigramis1_17,
    trigramis1_18,
    trigramis1_19,
    trigramis1_20,
    trigramis1_21,
    trigramis1_22,
    trigramis1_23,
    trigramis1_24,
    trigramis1_25,
    trigramis1_26,
    trigramis1_27,
    trigramis1_28,
    trigramis1_29,
    trigramis1_30,
    trigramis1_31,
    trigramis1_32,
    trigramis1_33,
    trigramis2_0,
    trigramis2_1,
    trigramis2_2,
    trigramis2_3,
    trigramis2_4,
    trigramis2_5,
    trigramis2_6,
    trigramis2_7,
    trigramis2_8,
    trigramis2_9,
    trigramis2_10,
    trigramis2_11,
    trigramis2_12,
    trigramis2_13,
    trigramis2_14,
    trigramis2_15,
    trigramis2_16,
    trigramis2_17,
    trigramis2_18,
    trigramis2_19,
    trigramis2_20,
    trigramis2_21,
    trigramis2_22,
    trigramis2_23,
    trigramis2_24,
    trigramis2_25,
    trigramis2_26,
    trigramis2_27,
    trigramis2_28,
    trigramis2_29,
    trigramis2_30,
    trigramis2_31,
    trigramis2_32,
    trigramis2_33,
    trigramis3_0,
    trigramis3_1,
    trigramis3_2,
    trigramis3_3,
    trigramis3_4,
    trigramis3_5,
    trigramis3_6,
    trigramis3_7,
    trigramis3_8,
    trigramis3_9,
    trigramis3_10,
    trigramis3_11,
    trigramis3_12,
    trigramis3_13,
    trigramis3_14,
    trigramis3_15,
    trigramis3_16,
    trigramis3_17,
    trigramis3_18,
    trigramis3_19,
    trigramis3_20,
    trigramis3_21,
    trigramis3_22,
    trigramis3_23,
    trigramis3_24,
    trigramis3_25,
    trigramis3_26,
    trigramis3_27,
    trigramis3_28,
    trigramis3_29,
    trigramis3_30,
    trigramis3_31,
    trigramis3_32,
    trigramis3_33,
    trigramis4_0,
    trigramis4_1,
    trigramis4_2,
    trigramis4_3,
    trigramis4_4,
    trigramis4_5,
    trigramis4_6,
    trigramis4_7,
    trigramis4_8,
    trigramis4_9,
    trigramis4_10,
    trigramis4_11,
    trigramis4_12,
    trigramis4_13,
    trigramis4_14,
    trigramis4_15,
    trigramis4_16,
    trigramis4_17,
    trigramis4_18,
    trigramis4_19,
    trigramis4_20,
    trigramis4_21,
    trigramis4_22,
    trigramis4_23,
    trigramis4_24,
    trigramis4_25,
    trigramis4_26,
    trigramis4_27,
    trigramis4_28,
    trigramis4_29,
    trigramis4_30,
    trigramis4_31,
    trigramis4_32,
    trigramis4_33,
    trigramis5_0,
    trigramis5_1,
    trigramis5_2,
    trigramis5_3,
    trigramis5_4,
    trigramis5_5,
    trigramis5_6,
    trigramis5_7,
    trigramis5_8,
    trigramis5_9,
    trigramis5_10,
    trigramis5_11,
    trigramis5_12,
    trigramis5_13,
    trigramis5_14,
    trigramis5_15,
    trigramis5_16,
    trigramis5_17,
    trigramis5_18,
    trigramis5_19,
    trigramis5_20,
    trigramis5_21,
    trigramis5_22,
    trigramis5_23,
    trigramis5_24,
    trigramis5_25,
    trigramis5_26,
    trigramis5_27,
    trigramis5_28,
    trigramis5_29,
    trigramis5_30,
    trigramis5_31,
    trigramis5_32,
    trigramis5_33,
    trigramis6_0,
    trigramis6_1,
    trigramis6_2,
    trigramis6_3,
    trigramis6_4,
    trigramis6_5,
    trigramis6_6,
    trigramis6_7,
    trigramis6_8,
    trigramis6_9,
    trigramis6_10,
    trigramis6_11,
    trigramis6_12,
    trigramis6_13,
    trigramis6_14,
    trigramis6_15,
    trigramis6_16,
    trigramis6_17,
    trigramis6_18,
    trigramis6_19,
    trigramis6_20,
    trigramis6_21,
    trigramis6_22,
    trigramis6_23,
    trigramis6_24,
    trigramis6_25,
    trigramis6_26,
    trigramis6_27,
    trigramis6_28,
    trigramis6_29,
    trigramis6_30,
    trigramis6_31,
    trigramis6_32,
    trigramis6_33,
    trigramis7_0,
    trigramis7_1,
    trigramis7_2,
    trigramis7_3,
    trigramis7_4,
    trigramis7_5,
    trigramis7_6,
    trigramis7_7,
    trigramis7_8,
    trigramis7_9,
    trigramis7_10,
    trigramis7_11,
    trigramis7_12,
    trigramis7_13,
    trigramis7_14,
    trigramis7_15,
    trigramis7_16,
    trigramis7_17,
    trigramis7_18,
    trigramis7_19,
    trigramis7_20,
    trigramis7_21,
    trigramis7_22,
    trigramis7_23,
    trigramis7_24,
    trigramis7_25,
    trigramis7_26,
    trigramis7_27,
    trigramis7_28,
    trigramis7_29,
    trigramis7_30,
    trigramis7_31,
    trigramis7_32,
    trigramis7_33,
    trigramis8_0,
    trigramis8_1,
    trigramis8_2,
    trigramis8_3,
    trigramis8_4,
    trigramis8_5,
    trigramis8_6,
    trigramis8_7,
    trigramis8_8,
    trigramis8_9,
    trigramis8_10,
    trigramis8_11,
    trigramis8_12,
    trigramis8_13,
    trigramis8_14,
    trigramis8_15,
    trigramis8_16,
    trigramis8_17,
    trigramis8_18,
    trigramis8_19,
    trigramis8_20,
    trigramis8_21,
    trigramis8_22,
    trigramis8_23,
    trigramis8_24,
    trigramis8_25,
    trigramis8_26,
    trigramis8_27,
    trigramis8_28,
    trigramis8_29,
    trigramis8_30,
    trigramis8_31,
    trigramis8_32,
    trigramis8_33,
    trigramis9_0,
    trigramis9_1,
    trigramis9_2,
    trigramis9_3,
    trigramis9_4,
    trigramis9_5,
    trigramis9_6,
    trigramis9_7,
    trigramis9_8,
    trigramis9_9,
    trigramis9_10,
    trigramis9_11,
    trigramis9_12,
    trigramis9_13,
    trigramis9_14,
    trigramis9_15,
    trigramis9_16,
    trigramis9_17,
    trigramis9_18,
    trigramis9_19,
    trigramis9_20,
    trigramis9_21,
    trigramis9_22,
    trigramis9_23,
    trigramis9_24,
    trigramis9_25,
    trigramis9_26,
    trigramis9_27,
    trigramis9_28,
    trigramis9_29,
    trigramis9_30,
    trigramis9_31,
    trigramis9_32,
    trigramis9_33,
    trigramis10_0,
    trigramis10_1,
    trigramis10_2,
    trigramis10_3,
    trigramis10_4,
    trigramis10_5,
    trigramis10_6,
    trigramis10_7,
    trigramis10_8,
    trigramis10_9,
    trigramis10_10,
    trigramis10_11,
    trigramis10_12,
    trigramis10_13,
    trigramis10_14,
    trigramis10_15,
    trigramis10_16,
    trigramis10_17,
    trigramis10_18,
    trigramis10_19,
    trigramis10_20,
    trigramis10_21,
    trigramis10_22,
    trigramis10_23,
    trigramis10_24,
    trigramis10_25,
    trigramis10_26,
    trigramis10_27,
    trigramis10_28,
    trigramis10_29,
    trigramis10_30,
    trigramis10_31,
    trigramis10_32,
    trigramis10_33,
    trigramis11_0,
    trigramis11_1,
    trigramis11_2,
    trigramis11_3,
    trigramis11_4,
    trigramis11_5,
    trigramis11_6,
    trigramis11_7,
    trigramis11_8,
    trigramis11_9,
    trigramis11_10,
    trigramis11_11,
    trigramis11_12,
    trigramis11_13,
    trigramis11_14,
    trigramis11_15,
    trigramis11_16,
    trigramis11_17,
    trigramis11_18,
    trigramis11_19,
    trigramis11_20,
    trigramis11_21,
    trigramis11_22,
    trigramis11_23,
    trigramis11_24,
    trigramis11_25,
    trigramis11_26,
    trigramis11_27,
    trigramis11_28,
    trigramis11_29,
    trigramis11_30,
    trigramis11_31,
    trigramis11_32,
    trigramis11_33,
    trigramis12_0,
    trigramis12_1,
    trigramis12_2,
    trigramis12_3,
    trigramis12_4,
    trigramis12_5,
    trigramis12_6,
    trigramis12_7,
    trigramis12_8,
    trigramis12_9,
    trigramis12_10,
    trigramis12_11,
    trigramis12_12,
    trigramis12_13,
    trigramis12_14,
    trigramis12_15,
    trigramis12_16,
    trigramis12_17,
    trigramis12_18,
    trigramis12_19,
    trigramis12_20,
    trigramis12_21,
    trigramis12_22,
    trigramis12_23,
    trigramis12_24,
    trigramis12_25,
    trigramis12_26,
    trigramis12_27,
    trigramis12_28,
    trigramis12_29,
    trigramis12_30,
    trigramis12_31,
    trigramis12_32,
    trigramis12_33,
    trigramis13_0,
    trigramis13_1,
    trigramis13_2,
    trigramis13_3,
    trigramis13_4,
    trigramis13_5,
    trigramis13_6,
    trigramis13_7,
    trigramis13_8,
    trigramis13_9,
    trigramis13_10,
    trigramis13_11,
    trigramis13_12,
    trigramis13_13,
    trigramis13_14,
    trigramis13_15,
    trigramis13_16,
    trigramis13_17,
    trigramis13_18,
    trigramis13_19,
    trigramis13_20,
    trigramis13_21,
    trigramis13_22,
    trigramis13_23,
    trigramis13_24,
    trigramis13_25,
    trigramis13_26,
    trigramis13_27,
    trigramis13_28,
    trigramis13_29,
    trigramis13_30,
    trigramis13_31,
    trigramis13_32,
    trigramis13_33,
    trigramis14_0,
    trigramis14_1,
    trigramis14_2,
    trigramis14_3,
    trigramis14_4,
    trigramis14_5,
    trigramis14_6,
    trigramis14_7,
    trigramis14_8,
    trigramis14_9,
    trigramis14_10,
    trigramis14_11,
    trigramis14_12,
    trigramis14_13,
    trigramis14_14,
    trigramis14_15,
    trigramis14_16,
    trigramis14_17,
    trigramis14_18,
    trigramis14_19,
    trigramis14_20,
    trigramis14_21,
    trigramis14_22,
    trigramis14_23,
    trigramis14_24,
    trigramis14_25,
    trigramis14_26,
    trigramis14_27,
    trigramis14_28,
    trigramis14_29,
    trigramis14_30,
    trigramis14_31,
    trigramis14_32,
    trigramis14_33,
    trigramis15_0,
    trigramis15_1,
    trigramis15_2,
    trigramis15_3,
    trigramis15_4,
    trigramis15_5,
    trigramis15_6,
    trigramis15_7,
    trigramis15_8,
    trigramis15_9,
    trigramis15_10,
    trigramis15_11,
    trigramis15_12,
    trigramis15_13,
    trigramis15_14,
    trigramis15_15,
    trigramis15_16,
    trigramis15_17,
    trigramis15_18,
    trigramis15_19,
    trigramis15_20,
    trigramis15_21,
    trigramis15_22,
    trigramis15_23,
    trigramis15_24,
    trigramis15_25,
    trigramis15_26,
    trigramis15_27,
    trigramis15_28,
    trigramis15_29,
    trigramis15_30,
    trigramis15_31,
    trigramis15_32,
    trigramis15_33,
    trigramis16_0,
    trigramis16_1,
    trigramis16_2,
    trigramis16_3,
    trigramis16_4,
    trigramis16_5,
    trigramis16_6,
    trigramis16_7,
    trigramis16_8,
    trigramis16_9,
    trigramis16_10,
    trigramis16_11,
    trigramis16_12,
    trigramis16_13,
    trigramis16_14,
    trigramis16_15,
    trigramis16_16,
    trigramis16_17,
    trigramis16_18,
    trigramis16_19,
    trigramis16_20,
    trigramis16_21,
    trigramis16_22,
    trigramis16_23,
    trigramis16_24,
    trigramis16_25,
    trigramis16_26,
    trigramis16_27,
    trigramis16_28,
    trigramis16_29,
    trigramis16_30,
    trigramis16_31,
    trigramis16_32,
    trigramis16_33,
    trigramis17_0,
    trigramis17_1,
    trigramis17_2,
    trigramis17_3,
    trigramis17_4,
    trigramis17_5,
    trigramis17_6,
    trigramis17_7,
    trigramis17_8,
    trigramis17_9,
    trigramis17_10,
    trigramis17_11,
    trigramis17_12,
    trigramis17_13,
    trigramis17_14,
    trigramis17_15,
    trigramis17_16,
    trigramis17_17,
    trigramis17_18,
    trigramis17_19,
    trigramis17_20,
    trigramis17_21,
    trigramis17_22,
    trigramis17_23,
    trigramis17_24,
    trigramis17_25,
    trigramis17_26,
    trigramis17_27,
    trigramis17_28,
    trigramis17_29,
    trigramis17_30,
    trigramis17_31,
    trigramis17_32,
    trigramis17_33,
    trigramis18_0,
    trigramis18_1,
    trigramis18_2,
    trigramis18_3,
    trigramis18_4,
    trigramis18_5,
    trigramis18_6,
    trigramis18_7,
    trigramis18_8,
    trigramis18_9,
    trigramis18_10,
    trigramis18_11,
    trigramis18_12,
    trigramis18_13,
    trigramis18_14,
    trigramis18_15,
    trigramis18_16,
    trigramis18_17,
    trigramis18_18,
    trigramis18_19,
    trigramis18_20,
    trigramis18_21,
    trigramis18_22,
    trigramis18_23,
    trigramis18_24,
    trigramis18_25,
    trigramis18_26,
    trigramis18_27,
    trigramis18_28,
    trigramis18_29,
    trigramis18_30,
    trigramis18_31,
    trigramis18_32,
    trigramis18_33,
    trigramis19_0,
    trigramis19_1,
    trigramis19_2,
    trigramis19_3,
    trigramis19_4,
    trigramis19_5,
    trigramis19_6,
    trigramis19_7,
    trigramis19_8,
    trigramis19_9,
    trigramis19_10,
    trigramis19_11,
    trigramis19_12,
    trigramis19_13,
    trigramis19_14,
    trigramis19_15,
    trigramis19_16,
    trigramis19_17,
    trigramis19_18,
    trigramis19_19,
    trigramis19_20,
    trigramis19_21,
    trigramis19_22,
    trigramis19_23,
    trigramis19_24,
    trigramis19_25,
    trigramis19_26,
    trigramis19_27,
    trigramis19_28,
    trigramis19_29,
    trigramis19_30,
    trigramis19_31,
    trigramis19_32,
    trigramis19_33,
    trigramis20_0,
    trigramis20_1,
    trigramis20_2,
    trigramis20_3,
    trigramis20_4,
    trigramis20_5,
    trigramis20_6,
    trigramis20_7,
    trigramis20_8,
    trigramis20_9,
    trigramis20_10,
    trigramis20_11,
    trigramis20_12,
    trigramis20_13,
    trigramis20_14,
    trigramis20_15,
    trigramis20_16,
    trigramis20_17,
    trigramis20_18,
    trigramis20_19,
    trigramis20_20,
    trigramis20_21,
    trigramis20_22,
    trigramis20_23,
    trigramis20_24,
    trigramis20_25,
    trigramis20_26,
    trigramis20_27,
    trigramis20_28,
    trigramis20_29,
    trigramis20_30,
    trigramis20_31,
    trigramis20_32,
    trigramis20_33,
    trigramis21_0,
    trigramis21_1,
    trigramis21_2,
    trigramis21_3,
    trigramis21_4,
    trigramis21_5,
    trigramis21_6,
    trigramis21_7,
    trigramis21_8,
    trigramis21_9,
    trigramis21_10,
    trigramis21_11,
    trigramis21_12,
    trigramis21_13,
    trigramis21_14,
    trigramis21_15,
    trigramis21_16,
    trigramis21_17,
    trigramis21_18,
    trigramis21_19,
    trigramis21_20,
    trigramis21_21,
    trigramis21_22,
    trigramis21_23,
    trigramis21_24,
    trigramis21_25,
    trigramis21_26,
    trigramis21_27,
    trigramis21_28,
    trigramis21_29,
    trigramis21_30,
    trigramis21_31,
    trigramis21_32,
    trigramis21_33,
    trigramis22_0,
    trigramis22_1,
    trigramis22_2,
    trigramis22_3,
    trigramis22_4,
    trigramis22_5,
    trigramis22_6,
    trigramis22_7,
    trigramis22_8,
    trigramis22_9,
    trigramis22_10,
    trigramis22_11,
    trigramis22_12,
    trigramis22_13,
    trigramis22_14,
    trigramis22_15,
    trigramis22_16,
    trigramis22_17,
    trigramis22_18,
    trigramis22_19,
    trigramis22_20,
    trigramis22_21,
    trigramis22_22,
    trigramis22_23,
    trigramis22_24,
    trigramis22_25,
    trigramis22_26,
    trigramis22_27,
    trigramis22_28,
    trigramis22_29,
    trigramis22_30,
    trigramis22_31,
    trigramis22_32,
    trigramis22_33,
    trigramis23_0,
    trigramis23_1,
    trigramis23_2,
    trigramis23_3,
    trigramis23_4,
    trigramis23_5,
    trigramis23_6,
    trigramis23_7,
    trigramis23_8,
    trigramis23_9,
    trigramis23_10,
    trigramis23_11,
    trigramis23_12,
    trigramis23_13,
    trigramis23_14,
    trigramis23_15,
    trigramis23_16,
    trigramis23_17,
    trigramis23_18,
    trigramis23_19,
    trigramis23_20,
    trigramis23_21,
    trigramis23_22,
    trigramis23_23,
    trigramis23_24,
    trigramis23_25,
    trigramis23_26,
    trigramis23_27,
    trigramis23_28,
    trigramis23_29,
    trigramis23_30,
    trigramis23_31,
    trigramis23_32,
    trigramis23_33,
    trigramis24_0,
    trigramis24_1,
    trigramis24_2,
    trigramis24_3,
    trigramis24_4,
    trigramis24_5,
    trigramis24_6,
    trigramis24_7,
    trigramis24_8,
    trigramis24_9,
    trigramis24_10,
    trigramis24_11,
    trigramis24_12,
    trigramis24_13,
    trigramis24_14,
    trigramis24_15,
    trigramis24_16,
    trigramis24_17,
    trigramis24_18,
    trigramis24_19,
    trigramis24_20,
    trigramis24_21,
    trigramis24_22,
    trigramis24_23,
    trigramis24_24,
    trigramis24_25,
    trigramis24_26,
    trigramis24_27,
    trigramis24_28,
    trigramis24_29,
    trigramis24_30,
    trigramis24_31,
    trigramis24_32,
    trigramis24_33,
    trigramis25_0,
    trigramis25_1,
    trigramis25_2,
    trigramis25_3,
    trigramis25_4,
    trigramis25_5,
    trigramis25_6,
    trigramis25_7,
    trigramis25_8,
    trigramis25_9,
    trigramis25_10,
    trigramis25_11,
    trigramis25_12,
    trigramis25_13,
    trigramis25_14,
    trigramis25_15,
    trigramis25_16,
    trigramis25_17,
    trigramis25_18,
    trigramis25_19,
    trigramis25_20,
    trigramis25_21,
    trigramis25_22,
    trigramis25_23,
    trigramis25_24,
    trigramis25_25,
    trigramis25_26,
    trigramis25_27,
    trigramis25_28,
    trigramis25_29,
    trigramis25_30,
    trigramis25_31,
    trigramis25_32,
    trigramis25_33,
    trigramis26_0,
    trigramis26_1,
    trigramis26_2,
    trigramis26_3,
    trigramis26_4,
    trigramis26_5,
    trigramis26_6,
    trigramis26_7,
    trigramis26_8,
    trigramis26_9,
    trigramis26_10,
    trigramis26_11,
    trigramis26_12,
    trigramis26_13,
    trigramis26_14,
    trigramis26_15,
    trigramis26_16,
    trigramis26_17,
    trigramis26_18,
    trigramis26_19,
    trigramis26_20,
    trigramis26_21,
    trigramis26_22,
    trigramis26_23,
    trigramis26_24,
    trigramis26_25,
    trigramis26_26,
    trigramis26_27,
    trigramis26_28,
    trigramis26_29,
    trigramis26_30,
    trigramis26_31,
    trigramis26_32,
    trigramis26_33,
    trigramis27_0,
    trigramis27_1,
    trigramis27_2,
    trigramis27_3,
    trigramis27_4,
    trigramis27_5,
    trigramis27_6,
    trigramis27_7,
    trigramis27_8,
    trigramis27_9,
    trigramis27_10,
    trigramis27_11,
    trigramis27_12,
    trigramis27_13,
    trigramis27_14,
    trigramis27_15,
    trigramis27_16,
    trigramis27_17,
    trigramis27_18,
    trigramis27_19,
    trigramis27_20,
    trigramis27_21,
    trigramis27_22,
    trigramis27_23,
    trigramis27_24,
    trigramis27_25,
    trigramis27_26,
    trigramis27_27,
    trigramis27_28,
    trigramis27_29,
    trigramis27_30,
    trigramis27_31,
    trigramis27_32,
    trigramis27_33,
    trigramis28_0,
    trigramis28_1,
    trigramis28_2,
    trigramis28_3,
    trigramis28_4,
    trigramis28_5,
    trigramis28_6,
    trigramis28_7,
    trigramis28_8,
    trigramis28_9,
    trigramis28_10,
    trigramis28_11,
    trigramis28_12,
    trigramis28_13,
    trigramis28_14,
    trigramis28_15,
    trigramis28_16,
    trigramis28_17,
    trigramis28_18,
    trigramis28_19,
    trigramis28_20,
    trigramis28_21,
    trigramis28_22,
    trigramis28_23,
    trigramis28_24,
    trigramis28_25,
    trigramis28_26,
    trigramis28_27,
    trigramis28_28,
    trigramis28_29,
    trigramis28_30,
    trigramis28_31,
    trigramis28_32,
    trigramis28_33,
    trigramis29_0,
    trigramis29_1,
    trigramis29_2,
    trigramis29_3,
    trigramis29_4,
    trigramis29_5,
    trigramis29_6,
    trigramis29_7,
    trigramis29_8,
    trigramis29_9,
    trigramis29_10,
    trigramis29_11,
    trigramis29_12,
    trigramis29_13,
    trigramis29_14,
    trigramis29_15,
    trigramis29_16,
    trigramis29_17,
    trigramis29_18,
    trigramis29_19,
    trigramis29_20,
    trigramis29_21,
    trigramis29_22,
    trigramis29_23,
    trigramis29_24,
    trigramis29_25,
    trigramis29_26,
    trigramis29_27,
    trigramis29_28,
    trigramis29_29,
    trigramis29_30,
    trigramis29_31,
    trigramis29_32,
    trigramis29_33,
    trigramis30_0,
    trigramis30_1,
    trigramis30_2,
    trigramis30_3,
    trigramis30_4,
    trigramis30_5,
    trigramis30_6,
    trigramis30_7,
    trigramis30_8,
    trigramis30_9,
    trigramis30_10,
    trigramis30_11,
    trigramis30_12,
    trigramis30_13,
    trigramis30_14,
    trigramis30_15,
    trigramis30_16,
    trigramis30_17,
    trigramis30_18,
    trigramis30_19,
    trigramis30_20,
    trigramis30_21,
    trigramis30_22,
    trigramis30_23,
    trigramis30_24,
    trigramis30_25,
    trigramis30_26,
    trigramis30_27,
    trigramis30_28,
    trigramis30_29,
    trigramis30_30,
    trigramis30_31,
    trigramis30_32,
    trigramis30_33,
    trigramis31_0,
    trigramis31_1,
    trigramis31_2,
    trigramis31_3,
    trigramis31_4,
    trigramis31_5,
    trigramis31_6,
    trigramis31_7,
    trigramis31_8,
    trigramis31_9,
    trigramis31_10,
    trigramis31_11,
    trigramis31_12,
    trigramis31_13,
    trigramis31_14,
    trigramis31_15,
    trigramis31_16,
    trigramis31_17,
    trigramis31_18,
    trigramis31_19,
    trigramis31_20,
    trigramis31_21,
    trigramis31_22,
    trigramis31_23,
    trigramis31_24,
    trigramis31_25,
    trigramis31_26,
    trigramis31_27,
    trigramis31_28,
    trigramis31_29,
    trigramis31_30,
    trigramis31_31,
    trigramis31_32,
    trigramis31_33,
    trigramis32_0,
    trigramis32_1,
    trigramis32_2,
    trigramis32_3,
    trigramis32_4,
    trigramis32_5,
    trigramis32_6,
    trigramis32_7,
    trigramis32_8,
    trigramis32_9,
    trigramis32_10,
    trigramis32_11,
    trigramis32_12,
    trigramis32_13,
    trigramis32_14,
    trigramis32_15,
    trigramis32_16,
    trigramis32_17,
    trigramis32_18,
    trigramis32_19,
    trigramis32_20,
    trigramis32_21,
    trigramis32_22,
    trigramis32_23,
    trigramis32_24,
    trigramis32_25,
    trigramis32_26,
    trigramis32_27,
    trigramis32_28,
    trigramis32_29,
    trigramis32_30,
    trigramis32_31,
    trigramis32_32,
    trigramis32_33,
    trigramis33_0,
    trigramis33_1,
    trigramis33_2,
    trigramis33_3,
    trigramis33_4,
    trigramis33_5,
    trigramis33_6,
    trigramis33_7,
    trigramis33_8,
    trigramis33_9,
    trigramis33_10,
    trigramis33_11,
    trigramis33_12,
    trigramis33_13,
    trigramis33_14,
    trigramis33_15,
    trigramis33_16,
    trigramis33_17,
    trigramis33_18,
    trigramis33_19,
    trigramis33_20,
    trigramis33_21,
    trigramis33_22,
    trigramis33_23,
    trigramis33_24,
    trigramis33_25,
    trigramis33_26,
    trigramis33_27,
    trigramis33_28,
    trigramis33_29,
    trigramis33_30,
    trigramis33_31,
    trigramis33_32,
    trigramis33_33
]