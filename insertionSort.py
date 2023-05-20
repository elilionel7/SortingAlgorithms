class Sorter:
  def __init__(self, arr):
     self.arr = arr
  def insertionSort(self):
    for i in range(1,len(self.arr)):
      k = i-1
      while k >= 0 and self.arr[k] > self.arr[k+1]: # this is to make sure that the k+1 is less than the kth, k-1, all the way to the first one.
        cur = self.arr[k]
        self.arr[k] = self.arr[k+1] # replacing kth with (k+1)the. I will need to save kth some where before I do that. Thats where the cur=arr[k] is needed
        self.arr[k+1] = cur
        k -= 1
    return self.arr
arr= [3,4,1,2,5]
sorter = Sorter(arr)
print(sorter.insertionSort())