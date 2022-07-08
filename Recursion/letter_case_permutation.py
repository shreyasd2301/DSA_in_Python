def letter_case(ip,op):
    if len(ip)==0:
        print(op)
        return
    if ip[0].isdigit():
        letter_case(ip[1:],op+ip[0])
    else: 
        letter_case(ip[1:],op+ip[0])
        letter_case(ip[1:],op+ip[0].upper())

letter_case("a1b2","")