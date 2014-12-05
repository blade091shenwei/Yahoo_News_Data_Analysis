#encoding=utf-8
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')

# words = {'a':2, 'b':4}
# 
# if words.get('c') == None:
#     words.setdefault('c',2)
# 
# words.update({'a': words.get('a')+2})
# 
# print words

dict = {'a':5 , 'b':1, 'c':10, 'd':7}
s = sorted(dict.iteritems(), \
       key=lambda d:d[1], reverse = False )
print s


