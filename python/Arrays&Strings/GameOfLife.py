import copy
class Solution:
    def get_next_state(self, history_board, i, j):
        """
        :type history_board: List[List[int]]
        :rtype: int result value
        """
        result = history_board[i][j]
        live_neighbours = self.check_neighbours(history_board, i, j)
        if history_board[i][j] == 0 and live_neighbours == 3:
            result = 1
        if history_board[i][j] == 1 and (live_neighbours < 2 or live_neighbours > 3):
            result = 0
        return result

    def check_neighbours(self, history_board, i, j):
        print("For i",i, "and j ",j)
        live_neighbours = 0
        rows = len(history_board)
        columns = len(history_board[0])
        for iN in range(i - 1, i + 2):
            for jN in range(j - 1, j + 2):
                if iN in range(0, rows) and jN in range(0, columns):
                    if history_board[iN][jN] == 1 and iN != i and iN != j:
                        live_neighbours += 1
        print(live_neighbours)
        return live_neighbours

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        history_board = copy.deepcopy(board)
        for i in range(0, len(history_board)):
            for j in range(0, len(history_board[0])):
                next_state = self.get_next_state(history_board, i, j)
                board[i][j] = next_state
        print(board)


Solution().gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])