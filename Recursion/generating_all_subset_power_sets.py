def sub_set_of_string(ip, io):
    if len(ip)==0:
        print(io)
        return
    sub_set_of_string(ip[1:], io)
    sub_set_of_string(ip[1:], ip[0]+io)
sub_set_of_string('abc','')
sub_set_of_string('abb','')