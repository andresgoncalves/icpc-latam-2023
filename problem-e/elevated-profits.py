
def parse_data(lines: list[str]):
  total, start = [int(n) for n in lines[0].split()]
  start -= 1
  matrix = [[] for i in range(total)]
  for line in lines[1:]:
    a, b = [int(n) - 1 for n in line.split()]
    matrix[a].append(b)
    matrix[b].append(a)
  if len(lines) != total:
    raise Exception("Invalid data")
  return total, start, matrix


def highest_profit(total: int, current: int, matrix: list[list[bool]], prev: int = -1, step: int = 1, visited: set[int] = set(), loop: int = 0):
  base_profit = 0
  max_profit = 0
  if current not in visited:
    visited = set(visited)
    visited.add(current)
    base_profit = step * (current + 1)
    for next in matrix[current]:
      profit = highest_profit(total, next, matrix, current, step + 1, visited) 
      if profit > max_profit:
        max_profit = profit
  else:
    if loop == total:
      return 0
    for next in matrix[current]:
      if prev != next:
        profit = highest_profit(total, next, matrix, current, step, visited, loop + 1) 
        if profit > max_profit:
          max_profit = profit
  return base_profit + max_profit

def main():
  from pathlib import Path
  with open(Path(__file__).parent.joinpath("./elevated-profits.txt")) as file:
    total, start, matrix = parse_data(file.readlines())
  print(highest_profit(total, start, matrix))

main()
