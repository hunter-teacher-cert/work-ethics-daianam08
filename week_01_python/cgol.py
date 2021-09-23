# C. Game of Life


#r=row c=col
board= [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]

# i=0
# for i in board:
#   print(board(i))
#   i=i+1


def board(r,c)
  total_neighbors = 0
  if r>0 && c>0:
    if board[r-1][c-1]=='X':
      total_neighbors=total_neighbors + 1
  if r>0:
    if board[r-1][c]=='X':
      total_neighbors=total_neighbors + 1
  if r>0 && c<24:
    if board[r-1][c+1]=='X':
      total_neighbors=total_neighbors + 1
  if c>0:
    if board[r][c-1]=='X':
      total_neighbors=total_neighbors + 1
  if c<24:
    if board[r][c+1]=='X':
      total_neighbors=total_neighbors + 1
  if c>0 && r<24:
    if board[r+1][c-1]=='X':
      total_neighbors=total_neighbors + 1
  if r<24:
    if board[r+1][c]=='X':
      total_neighbors=total_neighbors + 1
  if r<24 && c<24:
    if board[r+1][c+1]=='X':
      total_neighbors=total_neighbors + 1
  return total_neighbors