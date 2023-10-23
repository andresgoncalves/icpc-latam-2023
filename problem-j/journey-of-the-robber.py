
def parse_data(data: list[str]):
  total = int(data[0])
  matrix = [[] for i in range(total)]
  for road in data[1:]:
    a, b = [int(n) for n in road.split()]
    matrix[a - 1].append(b)
    matrix[b - 1].append(a)
  return total, matrix

def find_next(origin: int, matrix: list[list[int]], prev: int = -1, current: int = -1, depth: int = 0):
  if current < 0:
    current = origin
  
  best_city = min(filter(lambda next: next > origin, matrix[current - 1]), default=-1)

  if not best_city < 0:
    return best_city, depth
  
  best_depth = -1

  for next in matrix[current - 1]:
    if prev != next:
      next_best_city, next_depth = find_next(origin, matrix, current, next, depth + 1)
      if best_city < 0 or next_depth < depth or (next_depth == best_depth and next_best_city < best_city):
        best_city = next_best_city
        best_depth = next_depth

  if best_city < 0 and current == origin:
    best_city = current
    
  return best_city, depth
    

def main():
  from pathlib import Path
  with open(Path(__file__).parent.joinpath("./journey-of-the-robber.txt")) as file:
    total, matrix = parse_data(file.readlines())
  best_cities = [find_next(i, matrix)[0] for i in range(1, total + 1)]
  print(*best_cities, sep=" ")

main()
