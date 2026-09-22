class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)
        tree = [[1, [0] * k] for _ in range(4 * n)]
        def merge(left, right):
            left_prod, left_cnt = left
            right_prod, right_cnt = right
            prod = (left_prod * right_prod) % k
            cnt = [0] * k
            for r in range(k):
                cnt[r] += left_cnt[r]
            for r in range(k):
                new_r = (left_prod * r) % k
                cnt[new_r] += right_cnt[r]
            return [prod, cnt]
        def build(node, l, r):
            if l == r:
                value = nums[l] % k
                tree[node] = [value, [0] * k]
                tree[node][1][value] = 1
                return
            mid = (l + r) // 2
            build(2 * node + 1, l, mid)
            build(2 * node + 2, mid + 1, r)
            tree[node] = merge(
                tree[2 * node + 1],
                tree[2 * node + 2]
            )
        def update(node, l, r, index, value):
            if l == r:
                value %= k
                tree[node] = [value, [0] * k]
                tree[node][1][value] = 1
                return
            mid = (l + r) // 2
            if index <= mid:
                update(2 * node + 1, l, mid, index, value)
            else:
                update(2 * node + 2, mid + 1, r, index, value)
            tree[node] = merge(
                tree[2 * node + 1],
                tree[2 * node + 2]
            )
        def query(node, l, r, ql, qr):
            if qr < l or r < ql:
                return [1, [0] * k]
            if ql <= l and r <= qr:
                return tree[node]
            mid = (l + r) // 2
            left = query(2 * node + 1, l, mid, ql, qr)
            right = query(2 * node + 2, mid + 1, r, ql, qr)
            if qr <= mid:
                return left
            if ql > mid:
                return right
            return merge(left, right)
        build(0, 0, n - 1)
        answer = []
        for index, value, start, x in queries:
            update(0, 0, n - 1, index, value)
            result = query(0, 0, n - 1, start, n - 1)
            answer.append(result[1][x])

        return answer