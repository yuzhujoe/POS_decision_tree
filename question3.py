b1=set([")"])
b2=set([")","("])
b3=set([")","(",","])
b4=set([")","(",",","."])
b5=set([")","(",",",".",":"])
b6=set([")","(",",",":"])
b7=set([")","(","."])
b8=set([")","(",".",":"])
b9=set([")","(",":"])
b10=set([")",","])
b11=set([")",",","."])
b12=set([")",",",".",":"])
b13=set([")",",",":"])
b14=set([")","."])
b15=set([")",".",":"])
b16=set([")",":"])
b17=set(["("])
b18=set(["(",","])
b19=set(["(",",","."])
b20=set(["(",",",".",":"]
b21=set(["(",",",":"])
b22=set(["(","."])
b23=set(["(",".",":"])
b24=set(["(",":"])
b25=set([","])
b26=set([",","."])
b27=set([",",".",":"])
b28=set([",",":"])
b29=set(["."])
b30=set([".",":"])
b31=set([":"])

def isPunctuation1(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] in b1:
		return True
	else:
		return False

def isPunctuation2(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] in b2:
		return True
	else:
		return False

def isPunctuation3(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] in b3:
		return True
	else:
		return False

def isPunctuation4(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] in b4:
		return True
	else:
		return False

def isPunctuation5(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] in b5:
		return True
	else:
		return False

def isPunctuation6(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] in b6:
		return True
	else:
		return False

def isPunctuation7(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] in b7:
		return True
	else:
		return False

def isPunctuation8(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] in b8:
		return True
	else:
		return False

def isPunctuation9(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] in b9:
		return True
	else:
		return False

def isPunctuation10(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] in b10:
		return True
	else:
		return False

def isPunctuation11(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] in b11:
		return True
	else:
		return False

def isPunctuation12(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] in b12:
		return True
	else:
		return False

def isPunctuation13(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] in b13:
		return True
	else:
		return False

def isPunctuation14(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] in b14:
		return True
	else:
		return False

def isPunctuation15(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] in b15:
		return True
	else:
		return False

def isPunctuation16(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] in b16:
		return True
	else:
		return False

def isPunctuation17(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] in b17:
		return True
	else:
		return False

def isPunctuation18(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] in b18:
		return True
	else:
		return False

def isPunctuation19(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] in b19:
		return True
	else:
		return False

def isPunctuation20(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] in b20:
		return True
	else:
		return False

def isPunctuation21(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] in b21:
		return True
	else:
		return False

def isPunctuation22(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] in b22:
		return True
	else:
		return False

def isPunctuation23(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] in b23:
		return True
	else:
		return False

def isPunctuation24(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] in b24:
		return True
	else:
		return False

def isPunctuation25(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] in b25:
		return True
	else:
		return False

def isPunctuation26(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] in b26:
		return True
	else:
		return False

def isPunctuation27(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] in b27:
		return True
	else:
		return False

def isPunctuation28(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] in b28:
		return True
	else:
		return False

def isPunctuation29(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] in b29:
		return True
	else:
		return False

def isPunctuation30(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] in b30:
		return True
	else:
		return False

def isPunctuation31(corpus,i):
	if i == 0:
		return False
	if corpus[i-1] in b31:
		return True
	else:
		return False

question_list = [
	isPunctuation1,
	isPunctuation2,
	isPunctuation3,
	isPunctuation4,
	isPunctuation5,
	isPunctuation6,
	isPunctuation7,
	isPunctuation8,
	isPunctuation9,
	isPunctuation10,
	isPunctuation11,
	isPunctuation12,
	isPunctuation13,
	isPunctuation14,
	isPunctuation15,
	isPunctuation16,
	isPunctuation17,
	isPunctuation18,
	isPunctuation19,
	isPunctuation20,
	isPunctuation21,
	isPunctuation22,
	isPunctuation23,
	isPunctuation24,
	isPunctuation25,
	isPunctuation26,
	isPunctuation27,
	isPunctuation28,
	isPunctuation29,
	isPunctuation30,
	isPunctuation31
]