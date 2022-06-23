def sub_set_of_string(ip, op):
    if len(ip)==0:
        hash_map[op]=1
        return
    sub_set_of_string(ip[1:], ip[0]+op)
    sub_set_of_string(ip[1:], op)
hash_map={}
sub_set_of_string('abb','')
print(hash_map.keys())