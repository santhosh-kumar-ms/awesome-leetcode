def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        queue = [(entrance[0], entrance[1], 0)]
        maze[entrance[0]][entrance[1]] = '+'
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            x, y, steps = queue.pop(0)

            for ix, iy in directions:
                iix, iiy = x + ix, y + iy

                if 0 <= iix < rows and 0 <= iiy < cols and maze[iix][iiy] == '.':
                    if iix == 0 or iix == rows - 1 or iiy == 0 or iiy == cols - 1:
                        return steps + 1

                    maze[iix][iiy] = '+'
                    queue.append((iix, iiy, steps + 1))

        return -1 