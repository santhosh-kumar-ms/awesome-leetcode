def tribonacci(self, n: int) -> int:
        a, b, c = 1, 0, 0
        for _ in range(n): a, b, c = b, c, a + b + c
        return c
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        arr = [0] * (n + 1)
        arr[1] = 1
        arr[2] = 1
        for i in range(3, n + 1):
            arr[i] = arr[i - 3] + arr[i - 2] + arr[i - 1]
        return arr[n]
