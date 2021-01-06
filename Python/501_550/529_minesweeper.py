from typing import List


class Solution:
    def __init__(self):
        # 当前位置向周围扩展的八个方向
        self.dir_x = [0, 1, 0, -1, 1, 1, -1, -1]
        self.dir_y = [1, 0, -1, 0, 1, -1, 1, -1]
        # 记录地雷阵的长和宽
        self.m = None
        self.n = None

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x = click[0]
        y = click[1]
        self.n = len(board)
        self.m = len(board[0])

        # 如果一个地雷被挖出，把他修改为'X'，游戏结束，规则一
        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            self.dfs(board, x, y)

        return board

    def dfs(self, board, x, y):
        # 寻找周围的雷的数量
        count = 0
        for i in range(8):
            # 从周围8个方块中统计雷的数量
            tx = x + self.dir_x[i]
            ty = y + self.dir_y[i]
            if tx < 0 or tx >= self.n or ty < 0 or ty >= self.m:
                continue
            count += board[tx][ty] == 'M'

        if count:
            # 周围存在雷，规则三
            # 如果至少一个与地雷相邻的空方块'E'被挖出
            # 修改为数字'1'到'8'
            board[x][y] = chr(count + ord('0'))
        else:
            # 周围没有雷，规则二
            # 即没有相邻地雷的空方块'E'被挖出，修改为'B'
            # 并且所有和其相邻的未挖出的方块都应递归地揭露
            board[x][y] = 'B'
            for i in range(8):
                tx = x + self.dir_x[i]
                ty = y + self.dir_y[i]
                if tx < 0 or tx >= self.n or ty < 0 or ty >= self.m or board[tx][ty] != 'E':
                    continue
                self.dfs(board, tx, ty)


class Solution1:
    def __init__(self):
        # 当前位置向周围扩展的八个方向
        self.dir_x = [0, 1, 0, -1, 1, 1, -1, -1]
        self.dir_y = [1, 0, -1, 0, 1, -1, 1, -1]
        # 记录地雷阵的长和宽
        self.m = None
        self.n = None

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x = click[0]
        y = click[1]
        self.n = len(board)
        self.m = len(board[0])

        # 如果一个地雷被挖出，把他修改为'X'，游戏结束，规则一
        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            self.bfs(board, x, y)

        return board

    def bfs(self, board, i, j):
        visited = [[False] * self.m for i in range(self.n)]
        visited[i][j] = True
        queue = [(i, j)]
        while queue:
            x, y = queue.pop(0)

            # 寻找周围的雷的数量
            count = 0
            for k in range(8):
                # 从周围8个方块中统计雷的数量
                tx = x + self.dir_x[k]
                ty = y + self.dir_y[k]
                if tx < 0 or tx >= self.n or ty < 0 or ty >= self.m:
                    continue
                count += board[tx][ty] == 'M'

            if count:
                # 周围存在雷，规则三
                # 如果至少一个与地雷相邻的空方块'E'被挖出
                # 修改为数字'1'到'8'
                board[x][y] = chr(count + ord('0'))
            else:
                # 周围没有雷，规则二
                # 即没有相邻地雷的空方块'E'被挖出，修改为'B'
                # 并且所有和其相邻的未挖出的方块都应递归地揭露
                board[x][y] = 'B'
                for i in range(8):
                    tx = x + self.dir_x[i]
                    ty = y + self.dir_y[i]
                    if tx < 0 or tx >= self.n or ty < 0 or ty >= self.m or board[tx][ty] != 'E' or visited[tx][ty]:
                        continue
                    visited[tx][ty] = True
                    queue.append((tx, ty))


if __name__ == '__main__':
    board = [['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'M', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E']]
    click = [3, 0]
    print(Solution().updateBoard(board, click))
    print(Solution1().updateBoard(board, click))
