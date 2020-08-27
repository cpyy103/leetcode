from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 用来保存可用数字
        rows = [set(range(1, 10)) for i in range(9)]
        columns = [set(range(1, 10)) for i in range(9)]
        boxes = [set(range(1, 10)) for i in range(9)]

        # 用来保存需要填数字的位置
        empty = []
        # 删除行列格子中已经出现过的数字，并且记录需要填充的位置
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    rows[i].remove(num)
                    columns[j].remove(num)
                    boxes[(i // 3) * 3 + j // 3].remove(num)
                else:
                    empty.append((i, j))

        def back(k=0):
            if k == len(empty):  # 说明已经填到了最后，完成了数字填写
                return True
            i, j = empty[k]
            b = (i // 3) * 3 + j // 3
            for num in rows[i] & columns[j] & boxes[b]:
                rows[i].remove(num)
                columns[j].remove(num)
                boxes[b].remove(num)
                board[i][j] = str(num)

                if back(k + 1):
                    return True
                # 回溯，当前数字填写失败，将该数字加入到可用数字里
                rows[i].add(num)
                columns[j].add(num)
                boxes[b].add(num)

            # 返回上一个数字重新填写
            return False

        back()
        for i in board:
            print(i)


if __name__ == '__main__':
    board = [
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],

        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],

        ['.', '.', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9'],

    ]
    Solution().solveSudoku(board)
