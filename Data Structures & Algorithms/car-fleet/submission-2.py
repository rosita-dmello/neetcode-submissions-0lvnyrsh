class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = list(zip(position, speed))
        ps.sort(reverse=True)
        fleet = 1
        curr_t = (target - ps[0][0]) / ps[0][1]
        for i in range(1, len(ps)):
            t = (target - ps[i][0]) / ps[i][1]
            if t > curr_t:
                fleet += 1
                curr_t = t

        return fleet