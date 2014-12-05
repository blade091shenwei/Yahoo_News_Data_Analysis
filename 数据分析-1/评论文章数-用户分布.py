#encoding=utf-8
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')


if __name__ == "__main__":
    
    userDict = {}
    count = 0
    user = 'None'
    
    readFile = open('用户-评论过的文章', 'r')
    for line in readFile.xreadlines():
        if '%%%%' in line:
            userDict.setdefault(user, count) 
            user = line.replace('\n','')
            count = 0
        else:
            count = count + 1
    
    userDict_sorted = sorted(userDict.iteritems(),\
                key=lambda s:s[1], reverse = False)
    
    countDict = {}
    for user in userDict_sorted:
        if countDict.get(user[1]) == None:
            countDict.setdefault(user[1], 1)
        else:
            countDict.update({user[1]: \
                countDict.get(user[1]) + 1})
            
    writeFile = open('评论过的文章数-用户数', 'a')
    for k,v in countDict.iteritems():
        s = str(k) + ' ' + str(v) + '\n'
        writeFile.write(s)
    writeFile.close()
    readFile.close()
