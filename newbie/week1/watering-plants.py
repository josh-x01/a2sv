class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        current_capacity = capacity
        for i in range(len(plants)):
            if (plants[i] > capacity):
                return 0
            if (plants[i] > current_capacity):
                steps += (i) * 2 + 1
                current_capacity = capacity - plants[i]
                continue
            current_capacity -= plants[i]
            steps += 1
        return steps
