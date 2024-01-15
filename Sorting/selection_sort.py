class SelectionSort:
    def selection_sort(self, arr):
        if len(arr) <= 1:
            return arr
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[i]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
arr = [5,1,4,3,2,-1,8,0]
obj = SelectionSort()
obj.selection_sort(arr)
print(arr)