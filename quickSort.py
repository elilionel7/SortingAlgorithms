class Sorter:
  def __init__(self,arr): 
    self.arr = arr
  def quickSort(self,ln,rn): 
    if rn - ln + 1 <= 1:
      return self.arr
    pivot = self.arr[rn]
    j = ln
    for i in range(ln,rn): # placing all elements less than the pivot on the left and others on the right.
      if arr[i] < pivot:
        cur = arr[j]
        arr[j] = arr[i]
        arr[i] = cur
        j += 1

    arr[rn] = arr[j] #placing pivot in between left(small) and right(large)
    arr[j] = pivot
    self.quickSort(ln,j-1) # recursively call quicksort
    self.quickSort(j+1,rn)
    return self.arr

arr = [2,1,5,3,5,7,3,1,9]
sorter = Sorter(arr)
print(sorter.quickSort(0, len(sorter.arr) - 1))
