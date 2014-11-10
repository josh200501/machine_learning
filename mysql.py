# -*- coding: utf8 -*-
import MySQLdb
HOST='159.226.95.132'
USER='johnson'
PASSWD='291100'
PATH_TMP=r'd:/test/'
try:
    conn=MySQLdb.Connect(host=HOST,
                         user=USER,
                         passwd=PASSWD,
                         port=3306,
                         charset='utf8',
                         db='my_db')
    cur=conn.cursor()
    count=cur.execute('select dst from create_file')
    
    print 'there are %s rows record' %count
    res = []
    numrows=int(cur.rowcount)
    for x in xrange(0,numrows):
        r=cur.fetchone()
        res.append(r[0][:r[0].rindex('\\')]) #获取路径名  
        #print r[0]
    print res
    
    file_obj = open('res.txt','w')
    for x in xrange(0,numrows): 
        file_obj.writelines(res[x])
        file_obj.write('\n') #写入换行符
    file_obj.close() 
     
    print "complete..."
   
except MySQLdb.Error,e:
    print "Mysql Error %d: %s" %(e.args[0], e.args[1])
    
