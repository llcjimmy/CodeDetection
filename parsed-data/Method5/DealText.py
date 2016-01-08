import nltk
import math

stemmer = nltk.stem.porter.PorterStemmer()
tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
stopWord = nltk.corpus.stopwords.words('english')
stopwords = ['p', 'm', 'br', 'li', 'ul', 'ol', 'h', 'h2', 'h3', 'hr', 'dl', 'dd', 'dt', 'pi', 'pre', 'o', 'lt', 'gt', '|', '=', '+', '-', ';', '%', '~', '&']
stopwords.extend(stopWord)

def generateNoStemmed():
    ftrw = open('/Users/jimmy/StackOverflow/parsed-data/Method5/textNLTK.txt', 'w')
    
    f1 = open('/Users/jimmy/StackOverflow/parsed-data/Method5/text.txt', 'r')
    index = 0
    for line in f1:
        index += 1
        if index % 10000 == 0:
            print index

        line = line.strip()
        tokens = tokenizer.tokenize(line)
        words = [w.lower() for w in tokens if w.lower() not in stopwords]

        for word in words:
            ftrw.write(word + " ")
        ftrw.write("\n")

    ftrw.close()
    f1.close()

def generateStemmed():
    ftrw = open('/Users/jimmy/StackOverflow/parsed-data/Method5/textNLTKStemmed.txt', 'w')
    
    f1 = open('/Users/jimmy/StackOverflow/parsed-data/Method5/text.txt', 'r')
    index = 0
    for line in f1:
        index += 1
        if index % 10000 == 0:
            print index

        line = line.strip()
        tokens = tokenizer.tokenize(line)
        words = [w.lower() for w in tokens if w.lower() not in stopwords]
        words = [stemmer.stem(word) for word in words]

        for word in words:
            ftrw.write(word + " ")
        ftrw.write("\n")

    ftrw.close()
    f1.close()

def removelowfreqwordNoStemmed():
    globalDict = nltk.FreqDist()
    f1 = open('/Users/jimmy/StackOverflow/parsed-data/Method5/textNLTK.txt', 'r')
    for line in f1:
        line = line.strip()
        words = line.split()
        [globalDict.inc(word) for word in words]
    print len(globalDict)
    f1.close()

    num = 0
    for key in globalDict:
        if globalDict[key] > 1000:
            num += 1
    print num

    f1 = open('/Users/jimmy/StackOverflow/parsed-data/Method5/textNLTK.txt', 'r')
    f2 = open('/Users/jimmy/StackOverflow/parsed-data/Method5/textNLTKRemoveLowFreqWord.txt', 'w')
    for line in f1:
        line = line.strip()
        words = line.split()
        for word in words:
            if globalDict[word] > 1000:
                f2.write(word + " ")
        f2.write("\n")

    f1.close()
    f2.close()

def removelowfreqwordStemmed():
    globalDict = nltk.FreqDist()
    f1 = open('/Users/jimmy/StackOverflow/parsed-data/Method5/textNLTKStemmed.txt', 'r')
    for line in f1:
        line = line.strip()
        words = line.split()
        [globalDict.inc(word) for word in words]
    print len(globalDict)
    f1.close()

    num = 0
    for key in globalDict:
        if globalDict[key] > 1000:
            num += 1
    print num

    f1 = open('/Users/jimmy/StackOverflow/parsed-data/Method5/textNLTKStemmed.txt', 'r')
    f2 = open('/Users/jimmy/StackOverflow/parsed-data/Method5/textNLTKRemoveLowFreqWordStemmed.txt', 'w')
    for line in f1:
        line = line.strip()
        words = line.split()
        for word in words:
            if globalDict[word] > 1000:
                f2.write(word + " ")
        f2.write("\n")

    f1.close()
    f2.close()

def removelowfreqtag():
    globalDict = nltk.FreqDist()
    f1 = open('/Users/jimmy/StackOverflow/parsed-data/QuestionsTags.txt', 'r')
    for line in f1:
        line = line.strip()
        words = line.split("\t")
        [globalDict.inc(word) for word in words]
    print len(globalDict)
    f1.close()

    num = 0
    for key in globalDict:
        if globalDict[key] > 10:
            num += 1
    print num

    f1 = open('/Users/jimmy/StackOverflow/parsed-data/QuestionsTags.txt', 'r')
    f2 = open('/Users/jimmy/StackOverflow/parsed-data/Method5/QuestionsTagsRemoved.txt', 'w')
    for line in f1:
        line = line.strip()
        words = line.split("\t")
        for word in words:
            if globalDict[word] > 10:
                f2.write(word + "\t")
        f2.write("\n")
    f1.close()
    f2.close()

def bagofwords():
    globalDict = nltk.FreqDist()
    f1 = open('/Users/jimmy/StackOverflow/parsed-data/Method5/textNLTKRemoveLowFreqWordStemmed.txt', 'r')
    for line in f1:
        line = line.strip()
        words = line.split()
        [globalDict.inc(word) for word in words]
    print len(globalDict)
    f1.close()
    
    index = 1;
    dict = {};

    for key in globalDict:
        dict[key] = index
        index += 1
    print len(dict)

    f1 = open('/Users/jimmy/StackOverflow/parsed-data/Method5/textNLTKRemoveLowFreqWordStemmed.txt', 'r')
    f2 = open('/Users/jimmy/StackOverflow/parsed-data/Method5/QuestionsFeature.txt', 'w')
    index_line = 1
    for line in f1:
        line = line.strip()
        words = line.split()
        localDict = nltk.FreqDist()
        [localDict.inc(word) for word in words]
        for word in localDict:
            if word in dict:
                f2.write(str(index_line) + " " + str(dict[word]) + " " + str(localDict[word]))
                f2.write("\n")
        index_line += 1
    f1.close()
    f2.close()

def bagoftags():
    globalDict = nltk.FreqDist()
    f1 = open('/Users/jimmy/StackOverflow/parsed-data/Method5/QuestionsTagsRemoved.txt', 'r')
    for line in f1:
        line = line.strip()
        words = line.split("\t")
        [globalDict.inc(word) for word in words]
    print len(globalDict)
    f1.close()
    
    index = 1;
    dict = {};

    for key in globalDict:
        dict[key] = index
        index += 1
    print len(dict)

    f1 = open('/Users/jimmy/StackOverflow/parsed-data/Method5/tagIndex.txt', 'w')
    for key in dict:
        f1.write(key + ":" + str(dict[key]) + "\n")
    f1.close()

    f1 = open('/Users/jimmy/StackOverflow/parsed-data/Method5/QuestionsTagsRemoved.txt', 'r')
    f2 = open('/Users/jimmy/StackOverflow/parsed-data/Method5/QuestionsLabel.txt', 'w')
    index_line = 1
    for line in f1:
        line = line.strip()
        words = line.split("\t")
        localDict = nltk.FreqDist()
        [localDict.inc(word) for word in words]
        for word in localDict:
            if word in dict:
                f2.write(str(index_line) + " " + str(dict[word]) + " 1")
                f2.write("\n")
        index_line += 1
    f1.close()
    f2.close()

if __name__ == '__main__':
    #generateNoStemmed()
    #removelowfreqwordNoStemmed()
    #generateStemmed()
    #removelowfreqwordStemmed()

    #removelowfreqtag()
    #bagofwords()
    bagoftags()
