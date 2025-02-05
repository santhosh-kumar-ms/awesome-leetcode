def findMinArrowShots(self, points: List[List[int]]) -> int:
        arr = 0
        points.sort(key=lambda x : x[1])
        comp_pos = float('-inf')

        for i, j in points:
            if i > comp_pos:
                arr += 1
                comp_pos = j

        return arr