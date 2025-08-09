class Solution: 
    def selectionSort(self, arr):
        for i in range(len(arr)):
            idx = i
            for j in range(i + 1 , len(arr)):
                if arr[idx] > arr[j]:
                    idx = j
            arr[i] , arr[idx] = arr[idx] , arr[i]
        return arr
                
        
        
