#encoding=utf-8
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')

from lxml import html
import string 

if __name__ == "__main__":
    
    '评论字典，文件名-评论内容：up，文件名-评论内容：down'
    commentUpDict = {}
    commentDownDict = {}
    '文章字典，文件名：up，文件名：down'
    articleUpDict = {}
    articleDownDict = {}
    
    files = os.listdir('/home/blade091/EclipseProjects/数据分析-2/2-普通格式/')
    for fileName in files:
        filePath = '/home/blade091/EclipseProjects/数据分析-2/2-普通格式/' + fileName
        HTML = open(filePath).read()
        root = html.fromstring(HTML)
        alls = root.xpath('//comment|//reply')
        for all in alls:
            comment = all.text
            upcount = all.get('upcount')
            downcount = all.get('downcount')
            commentUpDict.setdefault(fileName + '%%%%' + comment, string.atoi(upcount)) 
            commentDownDict.setdefault(fileName + '%%%%' + comment, string.atoi(downcount)) 
            
            if articleUpDict.get(fileName) == None:
                articleUpDict.setdefault(fileName, string.atoi(upcount))
            else:
                articleUpDict.update({fileName:\
                                      articleUpDict.get(fileName) + string.atoi(upcount)})
                
            if articleDownDict.get(fileName) == None:
                articleDownDict.setdefault(fileName, string.atol(downcount))
            else:
                articleDownDict.update({fileName:\
                                      articleDownDict.get(fileName) + string.atol(downcount)})
    
    commentUpDict_sorted = sorted(commentUpDict.iteritems(), \
                    key = lambda s:s[1], reverse = True)
    commentDownDict_sorted = sorted(commentDownDict.iteritems(),\
                    key = lambda s:s[1], reverse = True)
    
    articleUpDict_sorted = sorted(articleUpDict.iteritems(), \
                    key = lambda s:s[1], reverse = True)
    articleDownDict_sorted = sorted(articleDownDict.iteritems(),\
                    key = lambda s:s[1], reverse = True)
    
    '生成up-评论数、down-评论数 柱状图曲线，选出前50条最热门评论（upcount最多）'
    upDict = {}
    for ele in commentUpDict_sorted:
        if upDict.get(ele[1]) == None:
            upDict.setdefault(ele[1], 1) 
        else:
            upDict.update({ele[1]:upDict.get(ele[1]) + 1})
    downDict = {}
    for ele in commentDownDict_sorted:
        if downDict.get(ele[1]) == None:
            downDict.setdefault(ele[1], 1) 
        else:
            downDict.update({ele[1]:downDict.get(ele[1]) + 1})
    '写入文件，按照评论的数目进行的排序，产生柱状图文件'
    upDict_sorted = sorted(upDict.iteritems(), \
                    key = lambda s:s[0], reverse = False)
    downDict_sorted = sorted(downDict.iteritems(), \
                    key = lambda s:s[0], reverse = False)
    writeFile = open('up-评论数曲线','a')
    for number in upDict_sorted:
        s = str(number[0]) + ' ' + str(number[1]) + '\n'
        writeFile.write(s) 
    writeFile.close()
    writeFile = open('down-评论数曲线','a')
    for number in downDict_sorted:
        s = str(number[0]) + ' ' + str(number[1]) + '\n'
        writeFile.write(s)
    writeFile.close()
    'upcount与downcount前50条评论的内容'
    writeFile = open('up-Top50','a')
    for ele in commentUpDict_sorted:
        s = str(ele[0]) + '%%%%' + str(ele[1]) + '\n'
        writeFile.write(s) 
    writeFile.close()
    writeFile = open('down-Top50','a')
    for ele in commentDownDict_sorted:
        s = str(ele[0]) + '%%%%' + str(ele[1]) + '\n'
        writeFile.write(s)
    writeFile.close()
    
    '文章-up-down 柱状图'
    writeFile = open('文章-up柱状图','a')
    for ele in articleUpDict_sorted:
        s = ele[0] + '%%%%' + str(ele[1]) + '\n'
        writeFile.write(s)
    writeFile.close()
    writeFile = open('文章-down柱状图','a')
    for ele in articleDownDict_sorted:
        s = ele[0] + '%%%%' + str(ele[1]) + '\n'
        writeFile.write(s)
    writeFile.close()
    
    
    
    
    