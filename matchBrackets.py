def isBalanced(leftItem, rightItem):
    if leftItem == '{' and rightItem == '}':
        return True
    elif leftItem == '(' and rightItem == ')':
        return True
    elif leftItem == '[' and rightItem == ']':
        return True
    else:
        return False

def is_matched(expression):
    stackS = []
    for eachElem in expression:
        if eachElem == "{" or eachElem == "[" or eachElem == "(":
            stackS.append(eachElem)
        else:
            if len(stackS) == 0:
                return False
            compareItem = stackS.pop()
            if not isBalanced(compareItem, eachElem):
                return False
    
    if len(stackS) == 0:
        return True
            
def match_brac(expression):
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"

bList = ('(([])){}')
match_brac(bList)
