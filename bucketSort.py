class Sorter:
  def __init__(self,arr):
    self.arr = arr
  def bucketSort(self):
    bucket = [0]*4 #range of values in the arr are 0,1,2,3. which is four unique [0]*4 == [0,0,0,0]

    for i in self.arr: 
      bucket[i] += 1 # taking frequencies of unique elements in arr eg if arr=[1,2,2,0,3,2,1,3,3,3] then bucket=[1,2,3,4] 
                      # note that the position in the bucket represents the unique elements in arr
    print('bucket ', bucket, ' containing frequencies of sorted arr ')
    k=0 #pointer to help update arr
    for j in range(len(bucket)): # j = 0,1,2,3 are the elements in the array, techniquecally sorted, right
      for _ in range(bucket[j]):         # helps to update j in arr the number of nums it appear
        self.arr[k] = j
        k += 1
    return self.arr
  #even though there is a nested for loop, I only have to traverse arr len(arr) times
arr = [3,1,1,3,2,0,1,3,2,0,0,2,2,1,2,3,3,3]
sorter = Sorter(arr)
print(sorter.bucketSort())