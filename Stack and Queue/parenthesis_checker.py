def parenthesis_checker(text):
    stack=[]
    for i in text:
        if i in ['(',"{","["]:
            stack.append(i)
        elif i in ["}",")","]"]:
            if len(stack)>0:
                alpha=stack.pop()
                if alpha=="[":
                    if i !="]":
                        return False
                if alpha=="(":
                    if i !=")":
                        return False    
                if alpha=="[":
                    if i !="]":
                        return False
    if stack:
        return False
    return True

parenthesis_checker("[(){}")