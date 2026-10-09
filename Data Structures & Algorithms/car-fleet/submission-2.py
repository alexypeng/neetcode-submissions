class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x: -x[0])

        latest_arrival = -1
        res = 0

        for position, speed in cars:
            arrival_time = -(-(target - position) // speed)
            if arrival_time > latest_arrival:
                res += 1
                latest_arrival = arrival_time
        
        return res
            