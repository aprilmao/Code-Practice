def max_con(arr):
  maxLen = 1
  arrDict = {}
  for eachElem in arr:
    arrDict[eachElem] = arrDict.get(eachElem, 0) + 1 
  for eachElem in arr:
    count = 1
    left = eachElem - 1
    right = eachElem + 1
    while left in arrDict:
      count += 1
      arrDict.pop(left)
      left -= 1
      
    while right in arrDict:
      count += 1
      arrDict.pop(right)
      right += 1

    if maxLen < count:
      maxLen = count
      
  return maxLen
  
arr = [1,2,3,1,2,3,4]
print max_con(arr)
