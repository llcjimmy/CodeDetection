import nltk
import math
import os

tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')

def generate():
    keyword_list = []
    path = '/Users/jimmy/StackOverflow/parsed-data/token'
    for root, dirs, files in os.walk(path):
        for filename in files:
            ftemp = open(os.path.join(root,filename), 'r')
            for line in ftemp:
                line = line.strip()
                if not line in keyword_list:
                    keyword_list.append(line)
            ftemp.close()
    print len(keyword_list)
    ftrw = open('/Users/jimmy/StackOverflow/parsed-data/Method2/data_train_2.arff', 'w')
    ftew = open('/Users/jimmy/StackOverflow/parsed-data/Method2/data_test_2.arff', 'w')
    ftrw.write("@relation token.traindata\n\n")
    ftew.write("@relation token.testdata\n\n")
    for keyword in keyword_list:
        ftrw.write("@attribute " + keyword + " numeric\n")
        ftew.write("@attribute " + keyword + " numeric\n")
    ftrw.write("@attribute languagetype {c#, c++, c, css, html, java, javascript, objective-c, php, perl, python, ruby, sql}\n\n@data\n")
    ftew.write("@attribute languagetype {c#, c++, c, css, html, java, javascript, objective-c, php, perl, python, ruby, sql}\n\n@data\n")

    f1 = open('/Users/jimmy/StackOverflow/parsed-data/QuestionsLanguageType.txt', 'r')
    index = 0
    for line in f1:
        line = line.strip()
        index += 1
        #if index > 100000:
        #    break

        filename = '/Users/jimmy/StackOverflow/parsed-data/code/Questions_'+str(index)+'_code.txt'
        f2 = open(filename, 'r')
        freq = [0] * len(keyword_list)
        for line2 in f2:
            #words = line2.split()
            words = tokenizer.tokenize(line2)
            for word in words:
                if word in keyword_list:
                    freq[keyword_list.index(word)] += 1
        f2.close()

        if index <= 413454:
            for fre in freq:
                ftrw.write(str(fre) + ",")
            ftrw.write(line + "\n")
        else:
            for fre in freq:
                ftew.write(str(fre) + ",")
            ftew.write(line + "\n")

    ftrw.close()
    ftew.close()
    f1.close()

if __name__ == '__main__':
    generate()
