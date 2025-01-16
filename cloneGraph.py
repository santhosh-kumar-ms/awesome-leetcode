def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = {}

        def cloneCall(node):
            if node in visited:
                return visited[node]

            dup = Node(node.val)
            visited[node] = dup

            for n in node.neighbors:
                dup.neighbors.append(cloneCall(n))
            return dup

        return cloneCall(node)