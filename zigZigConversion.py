def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        zig = [''] * numRows
        jump = 0
        curr_row = 0
        if numRows == 1 or n <= numRows:
            return s

        for c in s:
            zig[curr_row] += c
            if curr_row == 0:
                jump = 1
            elif curr_row == numRows - 1:
                jump = -1
            curr_row += jump

        return ''.join(zig)