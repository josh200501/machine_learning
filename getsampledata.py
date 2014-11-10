# -*- coding: utf8 -*-
import MySQLdb

def getdata(md5):
    #HOST='159.226.95.132'
    HOST = 'localhost'
    USER = 'johnson'
    PASSWD = '291100'
    
    res_arp = []
    res_createfile = []
    res_createkey = []
    res_createprocess = []
    res_createremoteprocess = []
    res_deletefile = []
    res_deletekey = []
    res_deletekeyvalue = []
    res_dns = []
    res_download = []
    res_icmp = []
    res_irc = []
    res_ircserver = []
    res_loaddriver = []
    res_overwritefile = []
    res_setkeyvalue = []
    res_tcp = []
    res_terminateprocess = []
    res_udp = []
    
    try:
        conn=MySQLdb.Connect(host=HOST,
                             user=USER,
                             passwd=PASSWD,
                             port=3306,
                             charset='utf8',
                             db='my_db')
        cur=conn.cursor()
        
        cur.execute('select spa from arp_list where md5=%s',md5)       
        numrows=int(cur.rowcount)
        for x in xrange(0,numrows):
            r=cur.fetchone()
            res_arp.append(r[0])   
        #-----------------------------------------------------------------------    
        cur.execute('select dst from create_file where md5=%s',md5)        
        numrows=int(cur.rowcount)
        for x in xrange(0,numrows):
            r=cur.fetchone()
            res_createfile.append(r[0][:r[0].rindex('\\')]) #获取路径名  
        #-----------------------------------------------------------------------
        cur.execute('select dst from create_key where md5=%s',md5)        
        numrows=int(cur.rowcount)
        for x in xrange(0,numrows):
            r=cur.fetchone()
            res_createkey.append(r[0][:r[0].rindex('\\')]) #获取路径名  
        #-----------------------------------------------------------------------
        cur.execute('select dst from create_process where md5=%s',md5)        
        numrows=int(cur.rowcount)
        for x in xrange(0,numrows):
            r=cur.fetchone()
            res_createprocess.append(r[0][:r[0].rindex('\\')]) #获取路径名  
        #-----------------------------------------------------------------------
        cur.execute('select dst from create_remote_process where md5=%s',md5)        
        numrows=int(cur.rowcount)
        for x in xrange(0,numrows):
            r=cur.fetchone()
            res_createremoteprocess.append(r[0]) 
        #-----------------------------------------------------------------------
        cur.execute('select dst from delete_file where md5=%s',md5)        
        numrows=int(cur.rowcount)
        for x in xrange(0,numrows):
            r=cur.fetchone()
            res_deletefile.append(r[0][:r[0].rindex('\\')]) #获取路径名  
        #-----------------------------------------------------------------------
        cur.execute('select dst from delete_key where md5=%s',md5)        
        numrows=int(cur.rowcount)
        for x in xrange(0,numrows):
            r=cur.fetchone()
            res_deletekey.append(r[0][:r[0].rindex('\\')]) #获取路径名  
        #-----------------------------------------------------------------------
        cur.execute('select dst from delete_key_value where md5=%s',md5)        
        numrows=int(cur.rowcount)
        for x in xrange(0,numrows):
            r=cur.fetchone()
            res_deletekeyvalue.append(r[0]) 
        #-----------------------------------------------------------------------
        cur.execute('select name from dns_query_list where md5=%s',md5)        
        numrows=int(cur.rowcount)
        for x in xrange(0,numrows):
            r=cur.fetchone()
            res_dns.append(r[0])  
        #-----------------------------------------------------------------------
        cur.execute('select file from download_list where md5=%s',md5)        
        numrows=int(cur.rowcount)
        for x in xrange(0,numrows):
            r=cur.fetchone()
            res_download.append(r[0])
        #-----------------------------------------------------------------------
        cur.execute('select dstip from icmp_list where md5=%s',md5)        
        numrows=int(cur.rowcount)
        for x in xrange(0,numrows):
            r=cur.fetchone()
            res_icmp.append(r[0])
        #-----------------------------------------------------------------------
        cur.execute('select dstip from irc_list where md5=%s',md5)        
        numrows=int(cur.rowcount)
        for x in xrange(0,numrows):
            r=cur.fetchone()
            res_irc.append(r[0])
        #-----------------------------------------------------------------------
        cur.execute('select dstip from irc_server_list where md5=%s',md5)        
        numrows=int(cur.rowcount)
        for x in xrange(0,numrows):
            r=cur.fetchone()
            res_ircserver.append(r[0]) 
        #-----------------------------------------------------------------------
        cur.execute('select dst from load_driver where md5=%s',md5)        
        numrows=int(cur.rowcount)
        for x in xrange(0,numrows):
            r=cur.fetchone()
            res_loaddriver.append(r[0])  
        #-----------------------------------------------------------------------
        cur.execute('select dst from overwrite_file where md5=%s',md5)        
        numrows=int(cur.rowcount)
        for x in xrange(0,numrows):
            r=cur.fetchone()
            res_overwritefile.append(r[0][:r[0].rindex('\\')]) #获取路径名  
        #-----------------------------------------------------------------------
        cur.execute('select dst from set_key_value where md5=%s',md5)        
        numrows=int(cur.rowcount)
        for x in xrange(0,numrows):
            r=cur.fetchone()
            res_setkeyvalue.append(r[0][:r[0].rindex('\\')]) #获取路径名  
        #-----------------------------------------------------------------------
        cur.execute('select dstip from tcp_list where md5=%s',md5)        
        numrows=int(cur.rowcount)
        for x in xrange(0,numrows):
            r=cur.fetchone()
            res_tcp.append(r[0])
        #-----------------------------------------------------------------------
        cur.execute('select dst from terminate_process where md5=%s',md5)        
        numrows=int(cur.rowcount)
        for x in xrange(0,numrows):
            r=cur.fetchone()
            res_terminateprocess.append(r[0]) 
        #-----------------------------------------------------------------------
        cur.execute('select dstip from udp_list where md5=%s',md5)        
        numrows=int(cur.rowcount)
        for x in xrange(0,numrows):
            r=cur.fetchone()
            res_udp.append(r[0])  
        #-----------------------------------------------------------------------
        cur.close()
        conn.close()
        
        return res_arp, res_createfile, res_createkey, res_createprocess,\
            res_createremoteprocess, res_deletefile, res_deletekey,\
            res_deletekeyvalue, res_dns, res_download, res_icmp, res_irc,\
            res_ircserver, res_loaddriver, res_overwritefile, res_setkeyvalue,\
            res_tcp, res_terminateprocess, res_udp

       
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" %(e.args[0], e.args[1])
    
if __name__ == '__main__':
    res_arp, res_createfile, res_createkey, res_createprocess,\
            res_createremoteprocess, res_deletefile, res_deletekey,\
            res_deletekeyvalue, res_dns, res_download, res_icmp, res_irc,\
            res_ircserver, res_loaddriver, res_overwritefile, res_setkeyvalue,\
            res_tcp, res_terminateprocess, res_udp = getdata()
            
    print   res_arp, res_createfile, res_createkey, res_createprocess,\
            res_createremoteprocess, res_deletefile, res_deletekey,\
            res_deletekeyvalue, res_dns, res_download, res_icmp, res_irc,\
            res_ircserver, res_loaddriver, res_overwritefile, res_setkeyvalue,\
            res_tcp, res_terminateprocess, res_udp
