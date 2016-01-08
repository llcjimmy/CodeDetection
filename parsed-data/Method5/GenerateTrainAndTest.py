import nltk
import math

def all():
    dict = {}
    f1 = open('/Users/jimmy/StackOverflow/parsed-data/Method5/tagIndex.txt', 'r')
    for line in f1:
        line = line.strip()
        words = line.split(":")
        dict[int(words[1])]=words[0]
    print len(dict)
    f1.close()

    f1 = open('/Users/jimmy/StackOverflow/parsed-data/Method5/MATAR/allresult.txt', 'r')
    f2 = open('/Users/jimmy/StackOverflow/parsed-data/Method5/all/QuestionsTagsAll.txt', 'w')
    for line in f1:
        line = line.strip()
        words = line.split("\t")
        [f2.write(dict[int(word)]+"\t") for word in words]
        f2.write("\n")
    f1.close()
    f2.close()

def last():
    dict = {}
    f1 = open('/Users/jimmy/StackOverflow/parsed-data/Method5/tagIndex.txt', 'r')
    for line in f1:
        line = line.strip()
        words = line.split(":")
        dict[int(words[1])]=words[0]
    print len(dict)
    f1.close()

    f1 = open('/Users/jimmy/StackOverflow/parsed-data/Method5/MATAR/lastresult.txt', 'r')
    f2 = open('/Users/jimmy/StackOverflow/parsed-data/Method5/last10percent/QuestionsTagsLast.txt', 'w')
    for line in f1:
        line = line.strip()
        words = line.split("\t")
        index = 0
        for word in words:
            index += 1
            if index <= 10:
                f2.write(dict[int(word)]+"\t")
        f2.write("\n")
    f1.close()
    f2.close()

def generate():
    ftrw = open('/Users/jimmy/StackOverflow/parsed-data/Method5/all/data_train.txt', 'w')
    ftew = open('/Users/jimmy/StackOverflow/parsed-data/Method5/all/data_test.txt', 'w')
    
    f1 = open('/Users/jimmy/StackOverflow/parsed-data/QuestionsLanguageType.txt', 'r')
    f2 = open('/Users/jimmy/StackOverflow/parsed-data/Method5/all/QuestionsTagsAll.txt', 'r')
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

def generate2try():
    ftrw = open('/Users/jimmy/StackOverflow/parsed-data/Method5/last10percent/data_train.txt', 'w')
    ftew = open('/Users/jimmy/StackOverflow/parsed-data/Method5/last10percent/data_test.txt', 'w')
    
    f1 = open('/Users/jimmy/StackOverflow/parsed-data/QuestionsLanguageType.txt', 'r')
    f2 = open('/Users/jimmy/StackOverflow/parsed-data/Method5/QuestionsTagsRemoved.txt', 'r')
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
    dict = []
    dict.append("c")
    dict.append("c++")
    dict.append("c#")
    dict.append("css")
    dict.append("html")
    dict.append("java")
    dict.append("javascript")
    dict.append("objective-c")
    dict.append("perl")
    dict.append("php")
    dict.append("python")
    dict.append("ruby")
    dict.append("sql")

    ftrw = open('/Users/jimmy/StackOverflow/parsed-data/Method5/last10percent/data_train.txt', 'w')
    ftew = open('/Users/jimmy/StackOverflow/parsed-data/Method5/last10percent/data_test.txt', 'w')
    
    f1 = open('/Users/jimmy/StackOverflow/parsed-data/QuestionsLanguageType.txt', 'r')
    f2 = open('/Users/jimmy/StackOverflow/parsed-data/Method5/QuestionsTagsRemoved.txt', 'r')
    f3 = open('/Users/jimmy/StackOverflow/parsed-data/Method5/last10percent/QuestionsTagsLast.txt', 'r')
    index = 0
    while(True):
        line = f1.readline()

        if (not line):
            break

        line = line.strip()
        index += 1

        if index <= 413454:
            line2 = f2.readline()
            if (not line2):
                break
            line2 = line2.strip()
            words = line2.split("\t")
            for word in words:
                ftrw.write(word + ",")
            ftrw.write(line + "\n")
        else:
            line3 = f3.readline()
            if (not line3):
                break
            line3 = line3.strip()
            words = line3.split("\t")
            if line in words:
                for word in words:
                    if not word in dict:
                        ftew.write(word + ",")
                    else:
                        if word == line:
                            ftew.write(word + ",")
            else:
                flag = 1
                for word in words:
                    if not word in dict:
                        ftew.write(word + ",")
                    else:
                        if flag:
                            ftew.write(word + ",")
                            flag = 0
                        
            ftew.write(line + "\n")

    ftrw.close()
    ftew.close()
    f1.close()
    f2.close()
    f3.close()

if __name__ == '__main__':
    #all()
    #last()
    #generate()
    #generate2try()
    generate2()