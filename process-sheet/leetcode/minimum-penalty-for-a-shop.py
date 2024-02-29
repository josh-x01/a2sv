class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ans=0
        prefix_y=[0]
        prefix_n=[0]
        for i in range(len(customers)):
            if customers[i]=="Y":
                prefix_y.append(prefix_y[-1]+1)
                prefix_n.append(prefix_n[-1])
            else:
                prefix_y.append(prefix_y[-1])
                prefix_n.append(prefix_n[-1]+1)
        prev=float("inf")
        for i in range(len(prefix_y)):
            curr=prefix_y[-1]-prefix_y[i]+prefix_n[i]
            if curr<prev:
                ans=i
                prev=curr
        return ans