import nltk
import math

#svm title
import os, sys
path = '/Users/jimmy/liblinear-2.1/python/'
sys.path.append(path)
from liblinearutil import *

stemmer = nltk.stem.porter.PorterStemmer()
tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
stopWord = nltk.corpus.stopwords.words('english')
stopwords = ['p', 'm', 'br', 'li', 'ul', 'ol', 'h', 'h2', 'h3', 'hr', 'dl', 'dd', 'dt', 'pi', 'pre', 'o', 'lt', 'gt', '|', '=', '+', '-', ';', '%', '~', '&']
stopwords.extend(stopWord)

def generate():
    ftrw = open('/Users/jimmy/StackOverflow/parsed-data/Method4/textNLTK.txt', 'w')
    
    f1 = open('/Users/jimmy/StackOverflow/parsed-data/Method4/text.txt', 'r')
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

def removelowfreqword():
    globalDict = nltk.FreqDist()
    f1 = open('/Users/jimmy/StackOverflow/parsed-data/Method4/textNLTK.txt', 'r')
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

    f1 = open('/Users/jimmy/StackOverflow/parsed-data/Method4/textNLTK.txt', 'r')
    f2 = open('/Users/jimmy/StackOverflow/parsed-data/Method4/textNLTKRemoveLowFreqWord.txt', 'w')
    for line in f1:
        line = line.strip()
        words = line.split()
        for word in words:
            if globalDict[word] > 1000:
                f2.write(word + " ")
        f2.write("\n")

    f1.close()
    f2.close()

def prepareDataFormatForTrainAndTest():
    globalDict = nltk.FreqDist()
    f1 = open('/Users/jimmy/StackOverflow/parsed-data/Method4/textNLTKRemoveLowFreqWord.txt', 'r')
    for line in f1:
        line = line.strip()
        words = line.split()
        [globalDict.inc(word) for word in words]
    print len(globalDict)
    f1.close()

    num = 1
    dict = {}
    for key in globalDict:
        dict[key] = num
        num += 1
    print len(dict)

    #f1 = open('/Users/jimmy/StackOverflow/parsed-data/Method4/textIndex.txt', 'w')
    #for key in dict:
    #    f1.write(key + ":" + str(dict[key]) + "\n")
    #f1.close()

    X = []

    f1 = open('/Users/jimmy/StackOverflow/parsed-data/Method4/textNLTKRemoveLowFreqWord.txt', 'r')
    for line in f1:
        line = line.strip()
        words = line.split()
        localDict = nltk.FreqDist()
        newdict = {}
        [localDict.inc(word) for word in words]
        for word in localDict:
            newdict[dict[word]] = localDict[word]
        X.append(newdict)
    print len(X)
    f1.close()

    #f1 = open('/Users/jimmy/StackOverflow/parsed-data/Method4/textDataFeature.txt', 'w')
    #for element in X:
    #    for key in element:
    #        f1.write(str(key) + ":" + str(element[key]) + " ")
    #    f1.write("\n")
    #f1.close()

    dict = {}
    dict["c"] = 2;
    dict["c++"] = 1;
    dict["c#"] = 0;
    dict["css"] = 3;
    dict["html"] = 4;
    dict["java"] = 5;
    dict["javascript"] = 6;
    dict["objective-c"] = 7;
    dict["perl"] = 9;
    dict["php"] = 8;
    dict["python"] = 10;
    dict["ruby"] = 11;
    dict["sql"] = 12;

    Y = []

    f1 = open('/Users/jimmy/StackOverflow/parsed-data/QuestionsLanguageType.txt', 'r')
    #f2 = open('/Users/jimmy/StackOverflow/parsed-data/Method4/textDataClass.txt', 'w')
    for line in f1:
        line = line.strip()
        Y.append(dict[line])
    #    f2.write(str(dict[line]) + "\n")
    f1.close()
    #f2.close()

    print "class deal over"

    return X, Y

def trainAndTestSVM():
    X, Y = prepareDataFormatForTrainAndTest()
    print "X, Y get"
    X_train = X[:413454]
    Y_train = Y[:413454]
    X_test = X[413454:]
    Y_test = Y[413454:]
    print "train and test splited"
    prob = problem(Y_train, X_train)
    param = parameter('-s 4')
    m = train(prob, param)

    print "training over"

    p_label, p_acc, p_val = predict(Y_test, X_test, m)

    print "predicting over"
    f1 = open('/Users/jimmy/StackOverflow/parsed-data/Method4/PredictedLabel2_new.txt', 'w')
    for element in p_label:
        f1.write(str(element) + "\n")
    f1.close()

if __name__ == '__main__':
    #generate()
    #removelowfreqword()
    #prepareDataFormatForTrainAndTest()
    trainAndTestSVM()
