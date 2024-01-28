class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res=[]
        for i in range(len(arr)-1,-1,-1):
            mx=i
            for j in range(i,-1,-1):
                if(arr[mx]<arr[j]):
                    mx=j
            self.flip(mx,arr)
            self.flip(i,arr)
            res.append(mx+1)
            res.append(i+1)
        return res

    def flip(self,end,arr):
        s=0
        while(s<end):
            arr[s],arr[end]=arr[end],arr[s]
            s+=1
            end-=1