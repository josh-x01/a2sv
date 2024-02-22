class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix_dict = defaultdict(int)

        for first, last, seat in bookings:
            prefix_dict[first] += seat
            prefix_dict[last+1] -= seat

        prefix = []
        for i in range(n):
            if i == 0:
                prefix.append(prefix_dict[i+1])
            else:
                prefix.append(prefix[-1] + prefix_dict[i+1])
        
        return prefix
