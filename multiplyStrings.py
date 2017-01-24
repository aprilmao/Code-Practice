def sameLen(str1,str2):
    if len(str1) > len(str2):
        diff = len(str1) - len(str2)
        str2 = "0" * diff  + str2
    elif len(str1) < len(str2):
        diff = len(str2) - len(str1) 
        str1 =  "0" * diff  + str1
    return str1,str2

def multStr(str1,str2):
    newStr = ""
    newNum = 0
    carry = 0
    str1 = str1[::-1]
    str2 = str2[::-1]
    for eachElem1 in range(len(str1)):
        newStr = ""
        for eachElem2 in range(len(str1)):
            comp1 = int(str1[eachElem2])
            comp2 = int(str2[eachElem1])
            multElem = ( comp1 * comp2 ) + carry
            if multElem == 9:
                carry = 0
            if multElem > 9:
                carry = multElem/10
                multElem =  multElem%10
            multElem = str(multElem)
            newStr = multElem + newStr
        newStr+="0" * eachElem1
        newNum += int(newStr)
    print newNum

#examples    
firstStr = "1234"
secStr = "14"
#make string same length
firstStr, secStr = sameLen(firstStr, secStr)
#multiply strings
multStr(firstStr, secStr)    