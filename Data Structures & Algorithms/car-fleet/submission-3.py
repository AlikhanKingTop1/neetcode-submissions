class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(zip(position,speed))
        pair.sort(reverse=True)
        fleets = 0
        slowest_t = 0
        for p,s in pair:
            curr_t = (target-p) / s
            if curr_t > slowest_t:
                fleets +=1
                slowest_t = curr_t
                
        return fleets