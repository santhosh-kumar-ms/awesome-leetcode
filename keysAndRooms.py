def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for k in rooms[node]:
                dfs(k)
        dfs(0)
        return len(visited) == len(rooms)