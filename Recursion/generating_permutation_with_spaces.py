def sub_set_of_string(ip, io):
    if len(ip)==0:
        print(io)
        return
    sub_set_of_string(ip[1:], io+" "+ip[0])
    sub_set_of_string(ip[1:], io+ip[0])
sub_set_of_string('bc','a')