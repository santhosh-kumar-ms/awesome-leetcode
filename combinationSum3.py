def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def helper(start, curr_arr, curr_val):
            if len(curr_arr) == k:
                if sum(curr_arr) == n:
                    res.append(curr_arr.copy())
                return
            
            for i in range(start, 10):
                curr_arr.append(i)
                helper(i + 1, curr_arr, curr_val + i)
                curr_arr.pop()
        helper(1, [], 0)
        return res