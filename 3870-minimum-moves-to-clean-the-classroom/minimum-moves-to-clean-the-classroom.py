from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m, n = len(classroom), len(classroom[0])
        litter = {}
        start = None
        k = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = k
                    k += 1

        target = (1 << k) - 1
        q = deque([(start[0], start[1], energy, 0, 0)])
        seen = {(start[0], start[1], energy, 0)}

        while q:
            r, c, e, mask, moves = q.popleft()

            if mask == target:
                return moves

            if e == 0:
                continue

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                if classroom[nr][nc] == 'X':
                    continue

                ne = e - 1
                if classroom[nr][nc] == 'R':
                    ne = energy

                nmask = mask
                if (nr, nc) in litter:
                    nmask |= 1 << litter[(nr, nc)]

                state = (nr, nc, ne, nmask)

                if state not in seen:
                    seen.add(state)
                    q.append((nr, nc, ne, nmask, moves + 1))

        return -1