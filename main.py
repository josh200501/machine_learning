# -*- coding: utf8 -*-
import local

a = u'c:\\windows\\rsa.dll'

b = a[a.rindex('\\')+1:]

c = a[:a.rindex('\\')]

'''
print a
print b
print c
'''
for key in local.behavior_type_list:
    print 'key=%s,\tvalue=%s'%(key,local.behavior_type_list[key])
    
a=[]
b=[1,2]
c=[3,4]
a.append(b)
a.append(c)
d=[0]*2
d[0]=5
d[1]=6
a.append(d)
d[0]=7
d[1]=8
a.append(d)
print a
print a[0]
print a[0][0]
print a[0][1]

at = ['ab','bc','cd','de','ef','fg']
test_dict = {}
j = 0
for i in at:
    test_dict[i] = j
    j=j+1
    
print test_dict
    