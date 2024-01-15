class QuickSort:
    def quick_sort(self, arr, left, right):
        if left < right:
            median = self.partition(arr, left, right)

            self.quick_sort(arr, left, median - 1)
            self.quick_sort(arr, median + 1, right)
    
    def partition(self, arr, left, right):
        pivot = arr[left]
        l = left + 1
        r = right
        done = False

        while not done:
            while l <= r and arr[l] < pivot:
                l += 1
            while l <= r and arr[r] > pivot:
                r -= 1
            if l > r:
                done = True
            else:
                arr[l], arr[r] = arr[r], arr[l]
        arr[left], arr[r] = arr[r], arr[left]
        return r

arr = [5,1,4,3,2,-1,8,0]
obj = QuickSort()
obj.quick_sort(arr, 0, len(arr)-1)
print(arr)

