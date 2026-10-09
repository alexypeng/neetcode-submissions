class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        latest_arrival = -1
        res = 0

        for i in range(len(position)):
            arrival_time = -(-(target - position[i]) // speed[i])
            if latest_arrival >= arrival_time:
                latest_arrival = min(latest_arrival, arrival_time)
            else:
                res += 1
                latest_arrival = arrival_time
        
        return res
            