def isBalanced(thing1, thing2):
    if thing1 == '(' and thing2 == ')':
        return True
    elif thing1 == '[' and thing2 == ']':
        return True
    elif thing1 == '{' and thing2 == '}':
        return True
    else:
        return False

def matchBrac(bracList):
    s1 = list()
    balanceString = True
    for eachBrac in bracList:
        if eachBrac == '(':
            s1.insert(0, '(')
        elif eachBrac == '[':
            s1.insert(0, '[')
        elif eachBrac == '{':
            s1.insert(0, '{')
        else:
            if len(s1) == 0:
                balanceString = False
            else:
                compareThis = s1.pop(0)
                balanceString = isBalanced(compareThis, eachBrac)

    if len(s1) == 0 and balanceString == True:
        print "It is balanced"
    else:
        print "Not balanced"
    return

bList = ('(([])){}')
matchBrac(bList)