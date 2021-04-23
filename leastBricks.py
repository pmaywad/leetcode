class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        if len(wall) == 0:
            return 0
        
        width_sum = sum(wall[0])
        crossing = {}
        untouched = 0
        for i in range(len(wall)):
            end = 0
            for j in range(len(wall[i])-1):
                end += wall[i][j]
                if crossing.get(end):
                    crossing[end] += 1
                else:
                    crossing[end] = 1
                untouched = max(untouched, crossing.get(end))
  
        return width_sum - untouched
