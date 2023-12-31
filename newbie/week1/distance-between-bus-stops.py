class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total_distance = 0
        if (start < destination):
            for i in range(start, destination):
                total_distance += distance[i]
        else:
            for i in range(destination, start):
                total_distance += distance[i]
        short_distance = min(total_distance, sum(distance)-total_distance)
        return short_distance


        