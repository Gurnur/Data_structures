class BubbleSort():
    def bubble_sort(self, arr):
        if len(arr) <= 1:
            return arr
        n = len(arr)
        swap = False
        for i in range(n):
            for j in range(i+1, n):
                if arr[j] < arr[i]:
                    arr[j], arr[i] = arr[i], arr[j]
                    swap = True
            if swap == False:
                return arr
        return arr

arr = [5,1,4,3,2,-1,8,0]
obj = BubbleSort()
print(obj.bubble_sort(arr))
