#encoding=utf-8
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')

from lxml import html
import string 

if __name__ == "__main__":
    
    '文章-回复数柱状图 、 用户-回复过的文章 、 回复文章数量-用户柱状图'
    articleDict = {}
    userDict = {}
    files = os.listdir('/home/blade091/EclipseProjects/数据分析-3/1-原始文件/')
    for fileName in files:
        filePath = '/home/blade091/EclipseProjects/数据分析-3/1-原始文件/' + fileName
        HTML = open(filePath).read()
        root = html.fromstring(HTML)
        users = root.xpath('//span[@class="int profile-link"]')
        
        for user in users:
            if articleDict.get(fileName) == None:
                articleDict.setdefault(fileName, 1)
            else:
                articleDict.update({fileName:\
                        articleDict.get(fileName) + 1})
                
            if userDict.get(user.get('data-guid')) == None:
                articleList = []
                articleList.append(fileName)
                userDict.setdefault(user.get('data-guid'),\
                                    articleList) 
            else:
                if fileName in userDict.get(user.get('data-guid')):
                    pass
                else:
                    articleList = userDict.get(user.get('data-guid'))
                    articleList.append(fileName)
                    userDict.update({user.get('data-guid'):\
                        articleList})
                
    articleDict_sorted = sorted(articleDict.iteritems(),\
                        key=lambda s:s[1], reverse = True)
    '写文件'
#     writeFile = open('文章-评论数','a')
#     for article in articleDict_sorted:
#         s = article[0] + '%%%%' + str(article[1]) + '\n'
#         writeFile.write(s)
#     writeFile.close()
    
    writeFile = open('用户-评论过的文章','a')
    for k,v in userDict.items():
        s = k + '%%%%' + '\n'
        writeFile.write(s)
        for article in v:
            writeFile.write(article)
            writeFile.write('\n')
        writeFile.write('%%%%') 
    writeFile.close()
    
    