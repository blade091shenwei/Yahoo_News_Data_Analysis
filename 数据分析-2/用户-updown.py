#encoding=utf-8
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')

from lxml import html
import string 

if __name__ == "__main__":
    
    userUpDict = {}
    userDownDict = {}
    files = os.listdir('/home/blade091/EclipseProjects/数据分析-2/1-原始文件/')
    for fileName in files:
        filePath = '/home/blade091/EclipseProjects/数据分析-2/1-原始文件/' + fileName
        HTML = open(filePath).read()
        root = html.fromstring(HTML)
        users = root.xpath('//span[@class="int profile-link"]')
        upcounts = root.xpath('//div[@id="up-vote-box"]/span')
        downcounts = root.xpath('//div[@id="down-vote-box"]/span')
        
        for user,upcount,downcount in zip(users, upcounts,downcounts):
            if userUpDict.get(user.text) == None:
                userUpDict.setdefault(user.get('data-guid'), string.atoi(upcount.text))
            else:
                userUpDict.update({user.get('data-guid'):\
                    userUpDict.get(user.get('data-guid')) + string.atoi(upcount.text)})
            
            if userDownDict.get(user.text) == None:
                userDownDict.setdefault(user.get('data-guid'), string.atoi(downcount.text))
            else:
                userDownDict.update({user.get('data-guid'):\
                    userDownDict.get(user.get('data-guid')) + string.atoi(downcount.text)})
            
    userUpDict_sorted = sorted(userUpDict.iteritems(),\
                               key=lambda s:s[1], reverse = True)
    userDownDict_sorted = sorted(userDownDict.iteritems(),\
                               key=lambda s:s[1], reverse = True)
    
    '生成柱状图文件'
    upDict = {}
    for user in userUpDict_sorted:
        if upDict.get(user[1]) == None:
            upDict.setdefault(user[1], 1) 
        else:
            upDict.update({user[1]: upDict.get(user[1]) + 1})
    downDict = {}
    for user in userDownDict_sorted:
        if downDict.get(user[1]) == None:
            downDict.setdefault(user[1], 1) 
        else:
            downDict.update({user[1]: upDict.get(user[1]) + 1})
            
    '写入文件'
    upDict_sorted = sorted(upDict.iteritems(), \
                           key=lambda s:s[0], reverse = False)
    downDict_sorted = sorted(downDict.iteritems(), \
                        key=lambda s:s[0], reverse = False)
    writeFile = open('up-用户数曲线','a')
    for number in upDict_sorted:
        s = str(number[0]) + ' ' + str(number[1]) + '\n'
        writeFile.write(s) 
    writeFile.close()
    writeFile = open('down-用户数曲线','a')
    for number in downDict_sorted:
        s = str(number[0]) + ' ' + str(number[1]) + '\n'
        writeFile.write(s)
    writeFile.close()
            
    