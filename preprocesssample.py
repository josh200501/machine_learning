# -*- coding: utf8 -*-
import getsampledata
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
def get_type_dict():
    j = 0
    for i in behavior_type_list:
        type_list_map[i]=j
        j=j+1
    return type_list_map
def get_behavior_dict(res):
    res2 = sorted(set(res),key=res.index) #去除重复项
    res_dict = {}
    j = 0
    for i in res2:
        res_dict[i] = j
        j = j+1
    return res_dict
def get_value_vector(res,name):
    type_map = get_type_dict()
    subtype_map = get_behavior_dict(res)
    #print subtype_map
    a = [0,0]
    b = []
    a[0] = type_map[name]
    for i in subtype_map:
        a[1] = subtype_map[i]
        b.append([a[0],a[1]])
    #print 'length of %s: %s' %(name,len(b))
    #print b
    return b
            
def final(md5):
    arp_list, create_file, create_key, create_process,\
    create_remote_process, delete_file, delete_key,\
    delete_key_value, dns_query_list, download_list, icmp_list, irc_list,\
    irc_server_list, load_driver, overwrite_file, set_key_value,\
    tcp_list, terminate_process, udp_list = getsampledata.getdata(md5)
    
    vector_sample = \
    get_value_vector(arp_list,'arp_list')+\
    get_value_vector(create_file,'create_file')+\
    get_value_vector(create_key,'create_key')+\
    get_value_vector(create_process,'create_process')+\
    get_value_vector(create_remote_process,'create_remote_process')+\
    get_value_vector(delete_file,'delete_file')+\
    get_value_vector(delete_key,'delete_key')+\
    get_value_vector(delete_key_value,'delete_key_value')+\
    get_value_vector(dns_query_list,'dns_query_list')+\
    get_value_vector(download_list,'download_list')+\
    get_value_vector(icmp_list,'icmp_list')+\
    get_value_vector(irc_list,'irc_list')+\
    get_value_vector(irc_server_list,'irc_server_list')+\
    get_value_vector(load_driver,'load_driver')+\
    get_value_vector(overwrite_file,'overwrite_file')+\
    get_value_vector(set_key_value,'set_key_value')+\
    get_value_vector(tcp_list,'tcp_list')+\
    get_value_vector(terminate_process,'terminate_process')+\
    get_value_vector(udp_list,'udp_list')
    
    #print vector_sample
    #print 'length of vector_sample(%s): %s'%(md5, len(vector_sample))
    return vector_sample

if __name__ == '__main__':
    print 'hello'
    md5 = 'febd2583e768f8812d1cf0d4e805565f'
    print md5
    final(md5)    