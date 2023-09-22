class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      for i in range(len(board)):
          row_set = set()
          clm_set = set()
          for k in range(len(board[i])):
              if board[i][k] != ".":
                  if board[i][k] in row_set:
                      return False
                  else:
                      row_set.add(board[i][k])
              if board[k][i] != ".":
                  if board[k][i] in clm_set:
                      return False
                  else:
                      clm_set.add(board[k][i])
      for i in range(0,8,3):
        for j in range(0,8,3):
          grid_set = set()
          for k in range(i, i+3):
            for l in range(j, j+3):
              if board[k][l] != ".":
                  if board[k][l] in grid_set:
                      return False
                  else:
                      grid_set.add(board[k][l])

      return True