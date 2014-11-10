# -*- coding: utf8 -*-
import MySQLdb

def getmd5():
    #HOST = '159.226.95.132'
    HOST = 'localhost'
    USER = 'johnson'
    PASSWD = '291100'
    
    md5 = []   
    try:
        conn=MySQLdb.Connect(host=HOST,
                             user=USER,
                             passwd=PASSWD,
                             port=3306,
                             charset='utf8',
                             db='my_db')
        cur=conn.cursor()
        cur.execute('select md5value from logs')       
        numrows=int(cur.rowcount)
        for x in xrange(0,numrows):
            r=cur.fetchone()
            md5.append(r[0])   

        cur.close()
        conn.close()
        #print 'length of md5list: ', len(md5)
        #print md5
        return md5
      
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" %(e.args[0], e.args[1])
    
if __name__ == '__main__':
    print 'hello'
    getmd5()
