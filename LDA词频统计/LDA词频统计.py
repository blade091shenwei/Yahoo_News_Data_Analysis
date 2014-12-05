#encoding=utf-8
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == "__main__":
    
    '构造词频字典，字典的key是一个个单词，存放的是单词的出现次数'
    wordsDict = {}
    readFile = open('articles', 'r')
    readFile.readline()
    for line in readFile.xreadlines():
        words = line.replace('\n','').split()
        
        for word in words:
            if wordsDict.get(word) == None:
                wordsDict.setdefault(word, 1)
            else:
                wordsDict.update({word: \
                                  wordsDict.get(word) + 1})
    
    writeFile = open('wordsFreq', 'a')
    '按照频率高低进行排序'
    wordsDict_sorted = sorted(wordsDict.iteritems(), \
                              key=lambda s:s[1], reverse = True)
#     for k,v in wordsDict_sorted.items():
#         print k,v
# #         writeFile.write(k + ' ' + str(v) + '\n')
    for word in wordsDict_sorted:
        writeFile.write(word[0] + ' ' + str(word[1]) + '\n')
    writeFile.close()
    readFile.close()