a = ['PRP$', 'VBG', 'VBD', 'VBN', 'POS', 'VBP', 'WDT', 'JJ', 'WP', 'VBZ', 'DT', 'RP', 'NN', ')', '(', ',', '.', 'TO', 'PRP', 'RB', ':', 'NNS', 'NNP', 'VB', 'WRB', 'CC', 'RBR', 'CD', 'EX', 'IN', 'MD', 'NNPS', 'JJS', 'JJR']

with open("question2.py","w") as f:
    for i in xrange(len(a)):
        f.write("def bigramis"+str(i)+"(corpus,i):\n\tif i == 0:\n\t\treturn False\n\tif corpus[i-1] == \""+a[i]+"\":\n\t\treturn True\n\telse:\n\t\treturn False\n\n")
