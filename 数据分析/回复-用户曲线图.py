#encoding=utf-8
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')

import string 

if __name__ == "__main__":
    
    '根据统计文件初始化字典'
    commentNumberDict = {}
    LargestNumber = 70
    for i in range(0, LargestNumber):
        commentNumberDict.setdefault(i, int(0))
    
    '由统计文件得到各个回复数量下，用户的数量'
    readFile = open('统计文件', 'r')
    for line in readFile.xreadlines():
        number = string.atoi(line.split()[1])
        commentNumberDict.update({number:\
                    commentNumberDict.get(number) + 1})
    
    writeFile = open('曲线文件', 'a')
    for k,v in commentNumberDict.iteritems():
        str1 = str(k) + ' ' + str(v) + '\n'
        writeFile.write(str1)
    
    writeFile.close()