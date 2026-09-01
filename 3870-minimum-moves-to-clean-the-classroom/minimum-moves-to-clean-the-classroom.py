from collections import deque
class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])
        start = None
        litter = {}
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = len(litter)
        if not litter:
            return 0
        total_litter = len(litter)
        target = (1 << total_litter) - 1
        q = deque()
        q.append((start[0], start[1], 0, energy, 0))
        visited = set()
        visited.add((start[0], start[1], 0, energy))
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        while q:
            r, c, mask, e, moves = q.popleft()
            if mask == target:
                return moves
            if e == 0:
                continue
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                if classroom[nr][nc] == 'X':
                    continue
                new_energy = e - 1
                new_mask = mask
                if classroom[nr][nc] == 'L':
                    idx = litter[(nr, nc)]
                    new_mask |= (1 << idx)
                if classroom[nr][nc] == 'R':
                    new_energy = energy
                state = (nr, nc, new_mask, new_energy)
                if state not in visited:
                    visited.add(state)
                    q.append((nr, nc, new_mask, new_energy, moves + 1))
        return -1