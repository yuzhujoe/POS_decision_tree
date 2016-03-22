def bigramis0(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == "PRP$":
		return True
	else:
		return False

def bigramis1(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == "VBG":
		return True
	else:
		return False

def bigramis2(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == "VBD":
		return True
	else:
		return False

def bigramis3(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == "VBN":
		return True
	else:
		return False

def bigramis4(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == "POS":
		return True
	else:
		return False

def bigramis5(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == "VBP":
		return True
	else:
		return False

def bigramis6(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == "WDT":
		return True
	else:
		return False

def bigramis7(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == "JJ":
		return True
	else:
		return False

def bigramis8(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == "WP":
		return True
	else:
		return False

def bigramis9(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == "VBZ":
		return True
	else:
		return False

def bigramis10(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == "DT":
		return True
	else:
		return False

def bigramis11(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == "RP":
		return True
	else:
		return False

def bigramis12(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == "NN":
		return True
	else:
		return False

def bigramis13(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == ")":
		return True
	else:
		return False

def bigramis14(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == "(":
		return True
	else:
		return False

def bigramis15(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == ",":
		return True
	else:
		return False

def bigramis16(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == ".":
		return True
	else:
		return False

def bigramis17(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == "TO":
		return True
	else:
		return False

def bigramis18(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == "PRP":
		return True
	else:
		return False

def bigramis19(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == "RB":
		return True
	else:
		return False

def bigramis20(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == ":":
		return True
	else:
		return False

def bigramis21(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == "NNS":
		return True
	else:
		return False

def bigramis22(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == "NNP":
		return True
	else:
		return False

def bigramis23(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == "VB":
		return True
	else:
		return False

def bigramis24(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == "WRB":
		return True
	else:
		return False

def bigramis25(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == "CC":
		return True
	else:
		return False

def bigramis26(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == "RBR":
		return True
	else:
		return False

def bigramis27(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == "CD":
		return True
	else:
		return False

def bigramis28(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == "EX":
		return True
	else:
		return False

def bigramis29(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == "IN":
		return True
	else:
		return False

def bigramis30(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == "MD":
		return True
	else:
		return False

def bigramis31(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == "NNPS":
		return True
	else:
		return False

def bigramis32(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == "JJS":
		return True
	else:
		return False

def bigramis33(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] == "JJR":
		return True
	else:
		return False

questionlist =[bigramis0,bigramis1]
