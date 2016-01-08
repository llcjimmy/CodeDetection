import nltk
import math

def generate():
    ftrw = open('/Users/jimmy/StackOverflow/parsed-data/Method3/data_train.txt', 'w')
    ftew = open('/Users/jimmy/StackOverflow/parsed-data/Method3/data_test.txt', 'w')
    
    f1 = open('/Users/jimmy/StackOverflow/parsed-data/QuestionsLanguageType.txt', 'r')
    f2 = open('/Users/jimmy/StackOverflow/parsed-data/QuestionsOtherTags.txt', 'r')
    index = 0
    while(True):
        line = f1.readline()
        line2 = f2.readline()

        if (not line) and (not line2):
            break

        line = line.strip()
        index += 1

        line2 = line2.strip()
        words = line2.split("\t")

        if index <= 413454:
            for word in words:
                ftrw.write(word + ",")
            ftrw.write(line + "\n")
        else:
            for word in words:
                ftew.write(word + ",")
            ftew.write(line + "\n")

    ftrw.close()
    ftew.close()
    f1.close()
    f2.close()

def generate2():
    globalDict = nltk.FreqDist()
    f1 = open('/Users/jimmy/StackOverflow/parsed-data/QuestionsOtherTags.txt', 'r')
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

    f1 = open('/Users/jimmy/StackOverflow/parsed-data/QuestionsOtherTags.txt', 'r')
    f2 = open('/Users/jimmy/StackOverflow/parsed-data/Method3/QuestionsOtherTagsRemoved.txt', 'w')
    for line in f1:
        line = line.strip()
        words = line.split("\t")
        for word in words:
            if globalDict[word] > 10:
                f2.write(word + "\t")
        f2.write("\n")
    f1.close()
    f2.close()

    ftrw = open('/Users/jimmy/StackOverflow/parsed-data/Method3/data_train_2.txt', 'w')
    ftew = open('/Users/jimmy/StackOverflow/parsed-data/Method3/data_test_2.txt', 'w')
    
    f1 = open('/Users/jimmy/StackOverflow/parsed-data/QuestionsLanguageType.txt', 'r')
    f2 = open('/Users/jimmy/StackOverflow/parsed-data/QuestionsOtherTags.txt', 'r')
    index = 0
    while(True):
        line = f1.readline()
        line2 = f2.readline()

        if (not line) and (not line2):
            break

        line = line.strip()
        index += 1

        line2 = line2.strip()
        words = line2.split("\t")

        if index <= 413454:
            for word in words:
                if globalDict[word] > 10:
                    ftrw.write(word + ",")
            ftrw.write(line + "\n")
        else:
            for word in words:
                if globalDict[word] > 10:
                    ftew.write(word + ",")
            ftew.write(line + "\n")

    ftrw.close()
    ftew.close()
    f1.close()
    f2.close()

def generate3():
    ftrw = open('/Users/jimmy/StackOverflow/parsed-data/Method3/data_train_3.txt', 'w')
    ftew = open('/Users/jimmy/StackOverflow/parsed-data/Method3/data_test_3.txt', 'w')
    
    f1 = open('/Users/jimmy/StackOverflow/parsed-data/QuestionsLanguageType.txt', 'r')
    f2 = open('/Users/jimmy/StackOverflow/parsed-data/QuestionsTags.txt', 'r')
    index = 0
    while(True):
        line = f1.readline()
        line2 = f2.readline()

        if (not line) and (not line2):
            break

        line = line.strip()
        index += 1

        line2 = line2.strip()
        words = line2.split("\t")

        if index <= 413454:
            for word in words:
                ftrw.write(word + ",")
            ftrw.write(line + "\n")
        else:
            for word in words:
                ftew.write(word + ",")
            ftew.write(line + "\n")

    ftrw.close()
    ftew.close()
    f1.close()
    f2.close()

if __name__ == '__main__':
    #generate()
    #generate2()
    generate3()