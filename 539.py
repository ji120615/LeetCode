class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        for timePoint in timePoints:
            time = 60 * int(timePoint[0:2]) + int(timePoint[3:5])
            times.append(time)
        
        times.sort()
        
        m = times[0] + 24 * 60 - times[-1]
        for i in range(len(times) - 1):
            m = min(m, times[i + 1] - times[i])

        return m