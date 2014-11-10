# -*- coding: utf8 -*-

behavior_type_list={'arp_list':'exist',
                    'create_file':'path',
                    'create_key':'path',
                    'create_process':'path',
                    'create_remote_process':'name',
                    'delete_file':'path',
                    'delete_key':'path',
                    'delete_key_value':'name',
                    'dns_query_list':'exist',
                    'download_list':'exist',
                    'icmp_list':'exist',
                    'irc_list':'exist',
                    'irc_server_list':'exist',
                    'load_driver':'exist',
                    'overwrite_file':'path',
                    'set_key_value':'name',
                    'tcp_list':'exist',
                    'terminate_process':'name',
                    'udp_list':'exist'}
type_list_map={}
def init():
    j = 0
    for i in behavior_type_list:
        type_list_map[i]=j
        j=j+1
    print type_list_map
    print type_list_map['delete_file']
    return type_list_map
def func():
    file_obj = open('res.txt','r')
    lines = file_obj.readlines()
    res = []
    for line in lines:
        line = line.strip()
        #print line
        res.append(line)
    file_obj.close() 
    print 'lenth of res: ',len(res)
    print res 
    print 'type of res: ',type(res)
    res2 = sorted(set(res),key=res.index)
    print 'lenth of res2: ',len(res2)
    print res2
    res_dict = {}
    j = 0
    for i in res2:
        res_dict[i] = j
        j = j+1
    print res_dict
    return res_dict
    print "complete..."
def final():
    type_map = init()
    subtype_map = func()
    print subtype_map
    a = [0,0]
    b = []
    a[0] = type_map['create_file']
    for i in subtype_map:
        a[1] = subtype_map[i]
        b.append([a[0],a[1]])
    #print b
    for i in b:
        print i
    #temp = [16,3]
    temp2 = [[16,3],[16,2],[16,5]]
    res = [0]*len(b)
    print res
    for i in temp2:
        if i in b:
            res[b.index(i)] = 1
            print 'index of [16,1]: ',b.index(i)
    print res
            
if __name__ == '__main__':
    final()
    #func()
    '''
    for key in behavior_type_list:
        print 'key=%s,\tvalue=%s'%(key,behavior_type_list[key])
    '''
    #init()