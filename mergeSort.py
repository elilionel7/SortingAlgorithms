class Sorter:
    def __init__(self, arr):
        self.arr = arr

    def merge(self, ln, mid, rn):
        L = self.arr[ln : mid + 1]
        R = self.arr[mid + 1 : rn + 1]
        i, j, k = 0, 0, ln 

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                self.arr[k] = L[i]
                i += 1
            else:
                self.arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            self.arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            self.arr[k] = R[j]
            j += 1
            k += 1

    def mergeSort(self, ln, rn):
        if rn - ln + 1 <= 1:
            return self.arr
        mid = (ln + rn)//2
        self.mergeSort(ln, mid)
        self.mergeSort(mid+1, rn)
        self.merge(ln, mid, rn)

        return self.arr

arr = [2,1,5,3,5,7,3,1,9]
sorter = Sorter(arr)
print(sorter.mergeSort(0, len(sorter.arr) - 1))
