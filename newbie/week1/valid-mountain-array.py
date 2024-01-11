class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        max1 = -1
        max2 = -1
        flag = False
        for i in range(1, len(arr)):
            if arr[i-1] == arr[i] and max1 == -1:
                return False
            if arr[i-1] < arr[i] and max2 == -1:
                max1 = arr[i]
            else:
                if max1 == -1:
                    break
                if max2 == -1:
                    max2 = arr[i]
                    # print(max2, max1)
                    if max2 == max1:
                        return False
                    continue
                if arr[i] >= max2:
                    max2 = -1
                    break
                max2 = arr[i]
        if max1 == -1 or max2 == -1:
            return False
        return True

                
        