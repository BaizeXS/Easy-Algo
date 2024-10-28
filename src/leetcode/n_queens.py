class Solution:
    def solveNQueens(self, n: int) -> list[list[list[str]]]:
        """求解 n 皇后"""

        def backtrack(
            row: int,
            n: int,
            state: list[list[str]],
            res: list[list[list[str]]],
            cols: list[bool],
            diags1: list[bool],
            diags2: list[bool],
        ):
            """回溯算法： n 皇后"""
            # 当放置完所有行时，记录解
            if row == n:
                res.append([list(row) for row in state])
                return
            # 遍历所有列
            for col in range(n):
                # 计算该格子对应的主对角线和次对角线
                diag1 = row - col + n - 1
                diag2 = row + col
                # 剪枝：不允许该格子所在列、主对角线、次对角线上存在皇后
                if not cols[col] and not diags1[diag1] and not diags2[diag2]:
                    # 尝试
                    state[row][col] = "Q"
                    cols[col] = diags1[diag1] = diags2[diag2] = True
                    # 放置下一行
                    backtrack(row + 1, n, state, res, cols, diags1, diags2)
                    # 回退
                    state[row][col] = "."
                    cols[col] = diags1[diag1] = diags2[diag2] = False

        # 初始化 n * n 大小的棋盘，其中 "Q" 代表皇后，"#" 代表空位
        state = [["." for _ in range(n)] for _ in range(n)]
        results = []
        cols = [False] * n
        diags1 = [False] * (2 * n - 1)  # 记录主对角线上是否有皇后
        diags2 = [False] * (2 * n - 1)  # 记录次对角线上是否有皇后
        backtrack(0, n, state, results, cols, diags1, diags2)
        res = [["".join(line) for line in result] for result in results]
        return res
