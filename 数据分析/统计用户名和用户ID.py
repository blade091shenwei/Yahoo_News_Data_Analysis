#encoding=utf-8
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')

from lxml import html

if __name__ == "__main__":
    
    userDict = {}
    files = os.listdir('/home/blade091/EclipseProjects/数据分析/1-原始文件/')
    for fileName in files:
        filePath = '/home/blade091/EclipseProjects/数据分析/1-原始文件/' + fileName
        HTML = open(filePath).read()
        root = html.fromstring(HTML)
        users = root.xpath('//span[@class="int profile-link"]')
        for user in users:
#             print user.text, user.get('data-guid')
            if userDict.get(user.get('data-guid')) \
                == None:
                userDict.setdefault(\
                    user.get('data-guid'), 1)
            else:
                userDict.update({user.get('data-guid'):\
                                 userDict.get(user.get('data-guid')) + 1})

    userDict_sorted = sorted(userDict.iteritems(), \
                             key=lambda s:s[1], reverse = True)
    writeFile = open('统计文件','a')
    for user in userDict_sorted:
        writeFile.write(user[0] + ' ' + str(user[1]) + '\n')
    writeFile.close()
                
        