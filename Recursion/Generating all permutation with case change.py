def recur(ip, op):
    if len(ip)==0:
        print(op)
        return
    recur(ip[1:], op +ip[0].upper())
    recur(ip[1:], op +ip[0].lower())

recur('abc','')