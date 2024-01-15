class MergeSort:
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        left_arr = self.merge_sort(left_arr)
        right_arr = self.merge_sort(right_arr)

        return self.merge(left_arr, right_arr)

    def merge(self, left, right):
        i, j = 0, 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        if left:
            result.extend(left[i:])
        if right:
            result.extend(right[j:])
        return result           

arr = [5,1,4,3,2,-1,8,0]
obj = MergeSort()
print(obj.merge_sort(arr))
