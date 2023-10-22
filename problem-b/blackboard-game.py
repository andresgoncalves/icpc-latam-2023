
def parse_data(data: list[str]):
  columns = int(data[0])
  board = [int(n) for n in data[1].split()]
  if len(board) != 3 * columns:
    raise Exception("Invalid data")
  return columns, board

def can_differ(board: list[int], difference: int = 0):
  if len(board) == 0:
    return difference != 0
  for i in board:
    i_board = list(board)
    i_board.remove(i)
    if not can_equalize(i_board, difference + i):
      return True
  return False
  
def can_equalize(board: list[int], difference: int = 0):
  if len(board) == 0:
    return difference == 0
  for i in board:
    i_board = list(board)
    i_board.remove(i)
    for j in i_board:
      j_board = list(i_board)
      j_board.remove(j)
      if not can_differ(j_board, difference - i):
        return True
  return False

def main():
  from pathlib import Path
  with open(Path(__file__).parent.joinpath("./blackboard-game.txt")) as file:
    columns, board = parse_data(file.readlines())
    print("Y" if can_differ(board) else "N")

main()
