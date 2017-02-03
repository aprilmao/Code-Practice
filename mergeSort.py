def merge(left, right):
  mergeArr = []
  i,j = 0, 0
  while len(mergeArr) < len(left) + len(right):
    if left[i] < right[j]:
      mergeArr.append(left[i])
      i += 1
    else:
      mergeArr.append(right[j])
      j += 1
    if i == len(left) or j == len(right):
      mergeArr.extend(left[i:] or right[j:])
      break
  return mergeArr

def mergeSort(arr):
  if len(arr) <= 1:
    return arr
  mid = len(arr) / 2
  left = mergeSort(arr[:mid])
  right = mergeSort(arr[mid:])
  return merge(left, right)
  
arr = [4,2,6,3,8,5]  
print mergeSort(arr)
