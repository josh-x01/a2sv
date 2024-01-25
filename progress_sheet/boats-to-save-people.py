class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        counter=0

        people.sort()
        start=0
        end=len(people)-1

        while(start<=end):           
            if start==end and people[start]<=limit:
                counter+=1
                start+=1
                end-=1
                
            elif people[start]+people[end]>limit:
                counter+=1
                end-=1
            elif people[start]+people[end]<=limit:
                counter+=1
                end-=1
                start+=1
                
        return counter