class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set(map(tuple, obstacles))

        DX = (0, 1, 0, -1)
        DY = (1, 0, -1, 0)

        d = 0
        curr = (0, 0)
        M = 0
        for command in commands:
            if command == -1:
                d = (d + 1) % 4
            elif command == -2:
                d = (d - 1) % 4
            else:
                for i in range(command):
                    temp = (curr[0] + DX[d], curr[1] + DY[d])
                    if temp in obstacles:
                        break
                    curr = temp

            M = max(M, curr[0] ** 2 + curr[1] ** 2)

        return M